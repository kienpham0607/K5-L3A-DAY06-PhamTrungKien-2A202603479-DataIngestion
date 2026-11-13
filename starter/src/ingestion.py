"""PDF extraction with physical page provenance, Unicode NFC and error records."""
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import re
import unicodedata
import pymupdf
from .models import DocumentPage

ROOT = Path(__file__).resolve().parents[2]


def normalize_text(text: str) -> str:
    """Join PDF line wraps; retain article, clause and heading boundaries."""
    text = unicodedata.normalize('NFC', text).replace('\u00ad', '').replace('\xa0', ' ')
    paragraphs: list[str] = []
    for raw in text.splitlines():
        line = re.sub(r'\s+', ' ', raw).strip()
        if not line or 'CÔNG BÁO/' in line or re.fullmatch(r'\d+', line):
            continue
        starts = re.match(r'^(?:Điều \d+\.|Chương [IVX]+\b|\d+\.\s|[a-zđ]\)\s)', line)
        if not paragraphs or starts or (line.isupper() and len(line) > 10):
            paragraphs.append(line)
        else:
            paragraphs[-1] += ' ' + line
    return '\n\n'.join(paragraphs)


def load_pdf(path: Path, document_id: str, source: str) -> list[DocumentPage]:
    with pymupdf.open(path) as document:
        return [DocumentPage(document_id, source, i + 1, normalize_text(p.get_text()))
                for i, p in enumerate(document)]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')


def load_corpus(manifest_path: Path, output: Path) -> tuple[list[DocumentPage], dict]:
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    pages, records, errors = [], [], []
    chapter = 'I'
    for entry in manifest['documents']:
        path = ROOT / entry['local_path']
        if sha256(path) != entry['sha256']:
            raise ValueError(f'Source checksum mismatch: {path}')
        raw_pages = load_pdf(path, entry['source_id'], entry['source_url'])
        if len(raw_pages) != entry['physical_pages']:
            raise ValueError(f'Physical page count mismatch: {path}')
        for page in raw_pages:
            if not page.text:
                errors.append({'document_id': page.document_id, 'page': page.page,
                               'status': 'excluded_no_extractable_text', 'ocr': False})
                continue
            if page.page not in entry['included_pages']:
                errors.append({'document_id': page.document_id, 'page': page.page,
                               'status': 'excluded_by_manifest'})
                continue
            records.append(asdict(page) | {'characters': len(page.text),
                                          'printed_page': entry['printed_page_start'] + page.page - 1})
            # Pages can contain two chapters. Split before chunking so chapter
            # filters never keep text from the wrong part of a boundary page.
            boundaries = list(re.finditer(r'(?m)^Chương ([IVX]+)\b', page.text))
            start = 0
            segments = []
            for match in boundaries:
                if match.start() > start:
                    segments.append((start, match.start(), chapter))
                start, chapter = match.start(), match.group(1)
            segments.append((start, len(page.text), chapter))
            for begin, end, section in segments:
                content = page.text[begin:end]
                leading = len(content) - len(content.lstrip())
                content = content.strip()
                if content:
                    metadata = {'section': section, 'law_id': '36/2024/QH15',
                                'version': 'original-2024', 'language': 'vi',
                                'page_offset': begin + leading,
                                'printed_page': entry['printed_page_start'] + page.page - 1}
                    pages.append(DocumentPage(page.document_id, page.source, page.page, content, metadata))
    count = len(records)
    if count < 30:
        raise ValueError(f'Need >=30 content pages, found {count}')
    for entry in manifest['documents']:
        found = [r['page'] for r in records if r['document_id'] == entry['source_id']]
        if found != entry['included_pages']:
            raise ValueError(f'Included pages missing for {entry["source_id"]}')
    summary = {'content_pages': count, 'segments': len(pages),
               'characters': sum(r['characters'] for r in records), 'errors': errors,
               'manifest_sha256': sha256(manifest_path)}
    write_jsonl(ROOT / 'data/processed/pages.jsonl', records)
    write_json(output / 'ingestion.json', summary)
    write_jsonl(output / 'ingestion_errors.jsonl', errors)
    return pages, summary
