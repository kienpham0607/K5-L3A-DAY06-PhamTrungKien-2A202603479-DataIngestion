"""Print physical page counts and article headings; never used as corpus labels."""
from pathlib import Path
import re
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
for path in sorted((ROOT / 'data/raw').glob('*.pdf')):
    for number, page in enumerate(PdfReader(path).pages, 1):
        text = page.extract_text() or ''
        (ROOT / f'artifacts/cache/{path.stem}-p{number}.txt').write_text(text, encoding='utf-8')
        headings = re.findall(r'Điều\s+\d+\.[^\n]*', text)
        print(path.name, number, len(text), ' | '.join(headings))
