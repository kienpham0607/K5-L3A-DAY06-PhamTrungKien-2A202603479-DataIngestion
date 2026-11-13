"""Two chunkers with stable IDs and offsets into normalized physical pages."""
import hashlib
import re
from .models import Chunk, DocumentPage


def _chunk(page: DocumentPage, start: int, end: int, method: str) -> Chunk:
    text = page.text[start:end]
    left = len(text) - len(text.lstrip())
    text = text.strip()
    absolute = page.metadata.get('page_offset', 0) + start + left
    identity = f'{page.document_id}:{page.page}:{absolute}:{method}:{text}'
    metadata = dict(page.metadata) | {'char_start': absolute, 'char_end': absolute + len(text),
                                    'chunk_method': method}
    return Chunk(hashlib.sha256(identity.encode('utf-8')).hexdigest()[:32],
                 page.document_id, page.source, page.page, text, metadata)


def fixed_size(page: DocumentPage, size: int, overlap: int) -> list[Chunk]:
    if size <= 0 or overlap < 0 or overlap >= size:
        raise ValueError('Require size > 0 and 0 <= overlap < size')
    chunks = []
    for start in range(0, len(page.text), size - overlap):
        end = min(start + size, len(page.text))
        if page.text[start:end].strip():
            chunks.append(_chunk(page, start, end, f'fixed-{size}-{overlap}'))
        if end == len(page.text):
            break
    return chunks


def by_paragraph(page: DocumentPage, max_size: int) -> list[Chunk]:
    """Pack legal paragraphs; split oversized clauses at sentence/word edges.

    No overlap; never cross physical page/chapter boundaries. Legal lists and
    continuation pages can still lack context; this is measured in the audit.
    """
    if max_size < 32:
        raise ValueError('max_size must be >=32')
    units = []
    for match in re.finditer(r'[^\n]+', page.text):
        start, end = match.span()
        while end - start > max_size:
            limit = start + max_size
            candidates = [m.end() for m in re.finditer(r'[.;!?]\s+', page.text[start:limit])]
            cut = start + candidates[-1] if candidates else page.text.rfind(' ', start + 1, limit)
            if cut <= start:
                cut = limit
            units.append((start, cut))
            start = cut
            while start < end and page.text[start].isspace():
                start += 1
        if start < end:
            units.append((start, end))
    spans = []
    for start, end in units:
        new_heading = re.match(r'(?:Điều \d+\.|Chương [IVX]+)', page.text[start:end])
        if spans and not new_heading and end - spans[-1][0] <= max_size:
            spans[-1] = (spans[-1][0], end)
        else:
            spans.append((start, end))
    return [_chunk(page, a, b, f'paragraph-{max_size}') for a, b in spans]
