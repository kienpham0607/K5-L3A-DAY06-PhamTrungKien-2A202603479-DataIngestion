"""Enter accepted labels from an existing, explicit student confirmation receipt.

This script never creates a confirmation or assumes consent from elapsed time.
The receipt and pinned draft/source hashes must already exist before it runs.
"""
import csv
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from starter.src.ingestion import sha256, write_json
from starter.src.run import check_frozen

OUT = ROOT / 'results/audit'


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows):
    with path.open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def verified_receipt(directory=OUT):
    path = directory / 'human_confirmation.json'
    receipt = json.loads(path.read_text(encoding='utf-8'))
    expected = {'evidence_questions':20, 'coherence_records':30,
                'grounding_records':15, 'metadata_records':45}
    if receipt.get('confirmed_scopes') != expected or not receipt.get('student_statement'):
        raise ValueError('Missing explicit confirmation for all required scopes')
    if not receipt.get('reviewer', '').strip() or not receipt.get('recorded_at_utc'):
        raise ValueError('Missing student reviewer or recorded time')
    hashes = receipt.get('reviewed_artifact_sha256', {})
    required = {f'results/audit/ai_{kind}.csv' for kind in ('coherence','grounding','metadata')}
    required |= {'benchmark/questions.json', 'benchmark/frozen_plan.json',
                 'starter/config.json', 'data/manifest.json',
                 'data/raw/36-2024-qh15-part1.pdf', 'data/raw/36-2024-qh15-part2.pdf',
                 'results/audit/review_corrections.json'}
    if not required <= set(hashes):
        raise ValueError('Confirmation receipt lacks draft/source snapshot hashes')
    for relative, expected_hash in hashes.items():
        target = (ROOT / relative).resolve()
        if not target.is_relative_to(ROOT.resolve()) or sha256(target) != expected_hash:
            raise ValueError(f'Reviewed artifact changed: {relative}; require a new student review')
    return receipt


def main():
    check_frozen()
    receipt = verified_receipt()
    reviewer = receipt['reviewer']
    reference = 'results/audit/human_confirmation.json'
    for kind in ('coherence', 'grounding', 'metadata'):
        drafts = read_csv(OUT / f'ai_{kind}.csv')
        existing = read_csv(OUT / f'manual_{kind}.csv')
        keys = ['strategy', 'sample_id'] if kind == 'coherence' else (
            ['strategy', 'question_id', 'rank'] if kind == 'metadata' else ['strategy', 'question_id'])
        original = {tuple(r[k] for k in keys):r for r in existing}
        label = 'complete_and_correct' if kind == 'metadata' else 'score'
        rows = []
        for draft in drafts:
            row = dict(draft)
            previous = original[tuple(row[k] for k in keys)]
            if previous['status'] == 'human_verified' and previous[label] != row[label]:
                raise ValueError('Existing human label differs from AI; preserve the human correction')
            reason = row['reason'].replace(
                'Đây là kiểm tra tự động + AI, chờ người học đối chiếu PDF.',
                'Đã được học viên đối chiếu PDF và chấp nhận sau kiểm tra tự động + AI.')
            row.update(reason='Học viên đã đối chiếu và đồng ý nhận xét AI: ' + reason,
                       reviewer=reviewer, status='human_verified',
                       label_origin='AI draft accepted after student source review',
                       confirmation_file=reference, confirmed_recorded_at_utc=receipt['recorded_at_utc'])
            rows.append(row)
        write_csv(OUT / f'manual_{kind}.csv', rows)
    evidence_path = OUT / 'evidence_review.json'
    evidence = json.loads(evidence_path.read_text(encoding='utf-8'))
    evidence.update(human_status='human_verified', human_reviewer=reviewer,
                    confirmation_record=reference, review_mode=receipt['review_mode'],
                    human_confirmation_recorded_at_utc=receipt['recorded_at_utc'])
    evidence_rows = []
    for row in evidence['rows']:
        row.update(human_status='human_verified', human_reviewer=reviewer,
                   answer_supported_human=True, confirmation_record=reference)
        evidence_rows.append({'question_id':row['question_id'], 'split':row['split'],
            'source_id':row['source_id'], 'page':row['page'], 'citation':row['citation'],
            'answer_supported':True, 'evidence_verified':True,
            'reason':'Học viên đối chiếu nguồn và đồng ý nhận xét AI: '+row['reason'],
            'reviewer':reviewer, 'status':'human_verified',
            'confirmation_file':reference,'confirmed_recorded_at_utc':receipt['recorded_at_utc']})
    write_json(evidence_path, evidence)
    write_csv(OUT / 'manual_evidence.csv', evidence_rows)
    checks_path = OUT / 'review_checks.json'
    checks = json.loads(checks_path.read_text(encoding='utf-8'))
    checks.update(human_confirmation_recorded=True, human_status='human_verified',
                  human_reviewer=reviewer, confirmation_record=reference)
    for row in checks['metadata_details']:
        row.update(human_status='human_verified', human_reviewer=reviewer)
    write_json(checks_path, checks)
    print('Recorded explicit student acceptance: 20 evidence questions and 90 audit records')


if __name__ == '__main__':
    main()
