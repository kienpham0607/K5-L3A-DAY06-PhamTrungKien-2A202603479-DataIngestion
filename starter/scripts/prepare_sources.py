"""Download official snapshots and write a reproducible page manifest (no benchmark)."""
from datetime import datetime
import json
from pathlib import Path
import sys
from urllib.request import urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.ingestion import ROOT, load_pdf, sha256, write_json

DOCUMENTS = [
    ('traffic-law-part1', '36-2024-qh15-part1.pdf', '36-2024-qh15.pdf', 76),
    ('traffic-law-part2', '36-2024-qh15-part2.pdf', '36-2024-qh15_tiep.pdf', 2),
]


def main():
    manifest_path = ROOT / 'data/manifest.json'
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        for entry in manifest['documents']:
            path = ROOT / entry['local_path']
            if not path.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
                with urlopen(entry['source_url'], timeout=60) as response:
                    path.write_bytes(response.read())
            if sha256(path) != entry['sha256']:
                raise ValueError('Official download changed: preserve the pinned snapshot; document a new corpus version')
        print('Existing manifest and source checksums verified; frozen metadata preserved')
        return
    documents = []
    for source_id, filename, remote, printed in DOCUMENTS:
        url = f'https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/9/{remote}'
        path = ROOT / 'data/raw' / filename
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            with urlopen(url, timeout=60) as response:
                path.write_bytes(response.read())
        pages = load_pdf(path, source_id, url)
        documents.append({
            'source_id': source_id, 'title': 'Luật Trật tự, an toàn giao thông đường bộ 36/2024/QH15 (bản gốc 2024)',
            'source_url': url, 'landing_url': 'https://vanban.chinhphu.vn/?classid=1&docid=211194&pageid=27160',
            'local_path': path.relative_to(ROOT).as_posix(), 'sha256': sha256(path),
            'accessed_at': datetime.now().astimezone().isoformat(),
            'license_or_permission': 'Văn bản quy phạm pháp luật; Điều 15 khoản 2 Luật Sở hữu trí tuệ: không thuộc phạm vi bảo hộ quyền tác giả. Chỉ dùng phần văn bản luật, ghi nguồn Cổng TTĐT Chính phủ.',
            'permission_reference': 'https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/9/155-vbhn-vpqh.pdf',
            'snapshot': 'Công báo ngày 24-8-2024; bản luật ban hành 27-06-2024, không phải bản hợp nhất cập nhật',
            'physical_pages': len(pages), 'printed_page_start': printed,
            'included_pages': [p.page for p in pages if p.text],
            'excluded_pages': [{'page': p.page, 'reason': 'Không có text trích xuất; không tính nội dung, không OCR'}
                               for p in pages if not p.text],
            'page_character_counts': {str(p.page): len(p.text) for p in pages},
        })
    write_json(ROOT / 'data/manifest.json', {
        'topic': 'Giao thông đường bộ Việt Nam — truy xuất Luật 36/2024/QH15 bản gốc',
        'count_rule': 'Trang vật lý PDF 1-based có nội dung luật trích xuất được; không nhân bản, không đếm trang không có text. Trang đầu có Điều 1 nên tính là nội dung. Số trang in Công báo là trường riêng.',
        'documents': documents,
    })
    print('Manifest written; content pages:', sum(len(d['included_pages']) for d in documents))


if __name__ == '__main__':
    main()
