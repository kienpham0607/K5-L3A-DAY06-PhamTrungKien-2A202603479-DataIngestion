"""Generate numeric tables from measured artifacts, with pending human audits explicit."""
import csv
import json
from pathlib import Path
from review_reporting import apply_confirmed_review, confirmed_summary

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'results/run'


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def main():
    dev,test=read(OUT/'metrics_dev.json'),read(OUT/'metrics_test.json')
    stats={r['strategy']:r for r in read(OUT/'index_stats.json')}
    audits=read(ROOT/'results/audit/draft_summary.json')
    selection=read(OUT/'selection.json')
    rows=dev+test
    table='| Strategy | Split | Hit@1 | Evidence Hit@3 | Chunks | Ingest (s) | API USD |\n|---|---|---|---|---|---|---|\n'
    for row in sorted(rows,key=lambda r:(r['strategy'],r['split'])):
        s=stats[row['strategy']]
        duration='Dùng chung B' if row['strategy']=='C' else f"{s['ingest_seconds']:.3f}"
        table+=f"| {row['strategy']} | {row['split']} | {row['hit1_count']}/{row['n']} ({row['hit1']:.1%}) | {row['hit3_count']}/{row['n']} ({row['hit3']:.1%}) | {s['chunk_count']} | {duration} | 0 |\n"
    audit_table='| Strategy | Coherence AI /2 (n=10) | Metadata tự động + AI | Tuân thủ filter test | Grounding AI: 0/1/2 (n=5); TB /2 |\n|---|---|---|---|---|\n'
    for r in audits:
        d=r['grounding_ai_distribution']
        audit_table+=f"| {r['strategy']} | {r['coherence_ai_mean']:.2f} | {r['metadata_auto_ai_correct']}/{r['metadata_n']} | {r['test_filter_compliant']}/{r['test_filter_n']} | {d['0']}/{d['1']}/{d['2']}; {r['grounding_ai_mean']:.2f} |\n"
    report=f'''# Báo cáo cá nhân — Day 06: Data Ingestion Engineering

**Học viên:** Phạm Trung Kiên · **MSSV:** 2A202603479 · **Lớp:** L3A (theo tên repo, cần học viên xác nhận).

**Đề tài:** Kho tri thức truy xuất về trật tự, an toàn giao thông đường bộ Việt Nam.

## 1. Dữ liệu và pipeline

Corpus là Luật 36/2024/QH15 bản ban hành năm 2024, lấy từ hai PDF trên [Cổng TTĐT Chính phủ](https://vanban.chinhphu.vn/?classid=1&docid=211194&pageid=27160). Đây là snapshot để thực nghiệm, không khẳng định là văn bản hợp nhất hiện hành năm 2026. Nguồn, ngày truy cập thực tế, hash SHA-256 và từng trang được ghi trong [manifest](../../data/manifest.json).

Hai file có 21 + 61 = 82 trang vật lý; dùng 20 + 61 = **81 trang nội dung**, {read(OUT/'ingestion.json')['characters']:,} ký tự sau chuẩn hóa. Trang vật lý 21 của phần 1 không trích được text; kiểm tra ảnh cho thấy chỉ là thông tin xuất bản, nên loại, không OCR. Trang 1 có Điều 1/2 nên được tính là nội dung, không phải trang bìa thuần túy. Không có mục lục/trang tham khảo thuần túy trong các trang được tính. Số trang PDF bắt đầu từ 1, **khác số trang in Công báo**: phần 1 trang 1 = Công báo 76; phần 2 trang 1 = Công báo 2.

Quyền sử dụng: văn bản quy phạm pháp luật không thuộc phạm vi bảo hộ quyền tác giả theo khoản 2 Điều 15 Luật Sở hữu trí tuệ, đối chiếu [bản hợp nhất của cơ quan nhà nước](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/9/155-vbhn-vpqh.pdf). Chỉ khai thác nội dung luật và ghi nguồn Chính phủ; không thu thập bài bình luận bên ngoài. Không gán giấy phép Creative Commons tự suy đoán.

Pipeline Python: PyMuPDF → Unicode NFC → bỏ header Công báo/số trang, nối dòng nhưng giữ Điều/khoản/điểm → chia tại ranh giới chương → chunk → embedding thật → Chroma lưu bền → cosine top-3 → benchmark/evidence trace. Có **89 segment nhưng chỉ 81 trang vật lý**, không đếm segment như trang mới. Chương được nhận từ tiêu đề nguồn và kế thừa liên tục giữa hai phần. Trang có hai chương được tách trước chunking để không gắn nhầm phạm vi. Không dùng OCR; lỗi/trang loại được lưu tại [ingestion_errors.jsonl](../../results/run/ingestion_errors.jsonl).

Model: **sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2**, revision `e8f8c211226b894fcb81acc59f3b34ba3efd5f42`, **384 chiều**, Sentence Transformers {read(OUT/'environment.json')['packages']['sentence-transformers']}, chạy CPU 4 thread, seed 42. Mean pooling của model, L2 normalize; không thêm prefix vào query/document. Cùng model/revision/cách encode cho cả A/B/C. Đặt `max_seq_length=256` cho cả query/document (khác mặc định 128 của model card; không vượt kiến trúc BERT). Đây là lựa chọn khóa trước dev. Đếm token thực tế: A tối đa {stats['A']['max_input_tokens']}, B/C tối đa {stats['B']['max_input_tokens']}; **0 chunk bị truncation** ở giới hạn đã chọn. Việc tăng giới hạn không đảm bảo chất lượng ngữ nghĩa, là một giới hạn của thực nghiệm. [Model card và giấy phép Apache-2.0](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2).

Store **Chroma {read(OUT/'environment.json')['packages']['chromadb']}**, `PersistentClient`, cosine HNSW **approximate**, ef_construction=200, ef_search=100, num_threads=1; cấu hình trong code và [environment.json](../../results/run/environment.json). Không tính cosine thuần Python thay store, không SQLite tự quản. Chroma có file SQLite nội bộ là cơ chế chính thức của backend. Collection A `traffic-fixed`; B và C cùng `traffic-paragraph`, bảo đảm B–C dùng đúng cùng chunk và vector. Index local ở `artifacts/chroma/`, bỏ khỏi Git; dựng lại từ model/corpus được pin. Model cũng không commit. Số liệu trace và metadata được lưu trong repo.

Metadata: `document_id`, `source` URL và `page` vật lý; bổ sung `section` (string số La Mã, từ tiêu đề chương), `law_id`, `version=original-2024`, `language=vi`, `printed_page`, `char_start/char_end` (offset ký tự Python trên trang chuẩn hóa). `section` là trường có ích để phân biệt phạm vi người hỏi yêu cầu; `source/page/offsets` cho phép mở đúng PDF và kiểm tra đoạn. Version là nhãn snapshot của dự án, không tuyên bố tình trạng hiệu lực hiện nay. Không dùng ID nguồn/trang gold làm filter.

## 2. Cấu hình, benchmark và kiểm soát thí nghiệm

| Cấu hình | Chunk | Retrieval |
|---|---|---|
| A | Fixed 500 ký tự, overlap 50 | Cosine top-3 không filter |
| B | Gom đoạn/khoản, tối đa 800 ký tự, overlap 0; đoạn dài tách ở câu/từ | Cosine top-3 không filter |
| C | Dùng chính chunk/vector/index B | Chỉ thêm filter `section` khi câu hỏi có phạm vi chương |

A–B so sánh **gói chiến lược chunking** (đổi cả cách chia, size và overlap), không kết luận riêng tác động từng tham số. **B–C chỉ thay một yếu tố là metadata filter**. Corpus/model/câu hỏi/metric/top-k/backend giữ cố định. Câu không filter của B/C có top-3 hoàn toàn giống nhau, đã kiểm tra từ trace.

Benchmark [questions.json](../../benchmark/questions.json) có **20 câu: Q01–Q15 dev, Q16–Q20 test**, có đáp án và evidence nằm thật tại trang nguồn. 7 câu có filter: dev Q01/Q13/Q14/Q15 và test Q18/Q19/Q20; tên chương được viết trực tiếp trong câu hỏi trước retrieval. Các chương I/II/IV/VII/IX có nội dung phân biệt; giá trị filter đối chiếu segment nguồn. Câu hỏi bao gồm trực tiếp, diễn đạt lại, điều kiện, ngoại lệ và quy định chuyển tiếp. Trình kiểm tra evidence exact sau chuẩn hóa whitespace thành công 20/20; Codex AI đọc nội dung nguồn để soạn đáp án, học viên vẫn cần kiểm chứng độc lập.

Split được khóa trước retrieval; cùng một luật có các chủ đề gần nhau giữa dev/test, Q16 và Q17 cùng trang. Vì thế đây là holdout câu hỏi nhỏ, không phải holdout tài liệu độc lập, không chứng minh khả năng tổng quát. Người soạn đã biết gold test lúc xây benchmark; chỉ **điểm retrieval test** được giữ chưa chạy đến sau lựa chọn dev. Frozen hash và vị trí mẫu được lưu tại [frozen_plan.json](../../benchmark/frozen_plan.json).

**Tiêu chí chọn trước test:** ưu tiên số câu dev Evidence Hit@3; nếu bằng thì Hit@1; tiếp theo ít chunk hơn; cuối cùng thứ tự A/B/C. Lựa chọn **{selection['chosen_strategy']}** được ghi lúc `{selection['selected_at_utc']}` trong [selection.json](../../results/run/selection.json), trước truy vấn test đầu tiên. Không đổi cấu hình/benchmark/model sau test. Các sửa hỗ trợ kiểm tra đường dẫn đa nền tảng, tài liệu và phiếu audit sau đó không thay kết quả truy xuất.

**Định nghĩa hit:** một trong top-k phải đúng file nguồn **và** trang gold, đồng thời chứa **toàn bộ** evidence đã ghi (bỏ khác biệt whitespace/NFC). Không tính hit chỉ vì chung trang/từ khóa; không ghép các mảnh nhiều chunk để thay metric bắt buộc. Adapter hỗ trợ alternative_gold nếu được xác minh, hiện chưa khai báo phương án bổ sung. Cách đo exact có thể bỏ sót diễn đạt tương đương; học viên có thể ghi nhận bằng review, không âm thầm đổi metric sau test.

## 3. Kết quả đo thật

{table}
Thời gian ingest gồm chunking, đếm token, embedding và upsert lần đầu; không gồm model load chung {stats['A']['model_load_seconds_shared']:.3f}s, tải model/PDF, lần upsert kiểm tra nạp lại hay benchmark. A/B lần đầu không dùng cache embedding; C dùng chung index nên **không có một lần embedding/ingest riêng**, không diễn giải 0 giây là hệ thống tức thời. Chi phí API là 0 USD vì toàn bộ suy luận chạy local; chưa định lượng điện, phần cứng và lưu lượng tải.

A có {stats['A']['total_characters']:,} ký tự trong chunk, {stats['A']['total_input_tokens_untruncated']:,} token đầu vào, median {stats['A']['median_characters']} ký tự; B/C có {stats['B']['total_characters']:,} ký tự, {stats['B']['total_input_tokens_untruncated']:,} token, median {stats['B']['median_characters']} ký tự. Overlap của A lặp thêm nội dung; B/C có ít hơn {stats['A']['chunk_count']-stats['B']['chunk_count']} chunk. Phân bố min/median/p95/max và số đo gốc nằm tại [index_stats.json](../../results/run/index_stats.json).

Nạp lại cùng dữ liệu: A **397 → 397**, B **310 → 310**; C dùng B. ID hash dựa trên tài liệu/trang/offset/cách chia/nội dung. Upsert rồi xóa ID lỗi thời trong collection khi đồng bộ **toàn corpus**; kiểm thử thay corpus xác nhận chunk cũ bị xóa. Các batch không có transaction toàn cục: nếu tiến trình lỗi giữa chừng phải nạp lại trước benchmark; không tuyên bố atomic update. Thay model/config embedding phải dùng thư mục index mới.

## 4. Đánh giá năm khía cạnh

**Trạng thái quan trọng:** bảng dưới đây là **nhãn nháp do Codex AI đọc và nhận xét**, metadata còn có kiểm tra nhất quán bằng code. **Chưa có học viên chấm thủ công/xác nhận**; không trình bày chúng như số liệu human audit. Chưa hoàn tất hạng mục audit thủ công của lab. Phiếu trống và hướng dẫn ở [results/audit](../../results/audit/README.md). Trạng thái máy đọc được: [manual_summary.json](../../results/audit/manual_summary.json).

{audit_table}
Rà soát bổ sung: [đối chiếu 20 câu với PDF](../../results/audit/EVIDENCE_REVIEW.md) ghi 20/20 evidence đúng trang và đáp án được nguồn hỗ trợ theo nhận xét AI; [gói đối chiếu audit](../../results/audit/AUDIT_REVIEW.md) cung cấp đủ text/nguồn cho 30 mẫu coherence, 15 grounding và 45 metadata. A/P04 được sửa nhãn AI 0 → 1 vì còn hiểu được một phần; coherence AI A thành 0,90/2. [Lịch sử sửa](../../results/audit/review_corrections.json) được công bố; frozen inputs và retrieval metrics giữ nguyên. Chưa ghi nhận học viên đã chấm thủ công.

1. **Retrieval:** A dev Hit@3 tốt nhất (10/15) nhưng Hit@1 thấp hơn B/C (4/15 so với 8/15). Test A/B đều 4/5, C 5/5. Một câu làm thay đổi 20 điểm phần trăm trên test; không kết luận C tốt nhất tổng quát.
2. **Coherence:** cùng 10 vị trí đã chọn trước retrieval: giữa trang chuẩn hóa của 10 trang nội dung đầu theo document_id/page. Chunk sớm nhất bao phủ offset là mẫu, không chọn mẫu theo điểm. A cắt giữa từ/câu; B/C giữ khoản tốt hơn nhưng vẫn thiếu tiêu đề cấm, danh sách hoặc ngữ cảnh ở trang tiếp nối. Nhãn 0/1/2 và lý do từng mẫu trong `ai_coherence.csv`; mẫu đầy đủ có text và offset trong `results/run/coherence_samples.json`. Phạm vi mẫu chỉ 10 trang đầu nên thiên về Chương I, không đại diện cả corpus. Không suy coherence từ Hit@3.
3. **Metadata:** đối chiếu 5 test × 3 rank × 3 cấu hình = 45 bản ghi. URL, page, offsets và section đều khớp nguồn/segment trong kiểm tra tự động + AI, nhưng người học chưa đối chiếu đủ PDF. Tỷ lệ tuân thủ yêu cầu filter là trên **câu hỏi**: A 1/3, B 1/3, C 3/3. A/B không áp dụng filter nên sự tuân thủ là tình cờ. `section` giúp sửa truy xuất sai phạm vi ở Q20; nó không phân biệt điều cụ thể cùng chương và không đảm bảo bằng chứng đủ. Nếu người dùng cung cấp nhầm chương, C có thể loại mất đáp án đúng; không tự đoán filter từ gold. Chưa thử trường hợp người dùng đưa filter sai.
4. **Grounding:** đọc top-3 của cùng 5 câu test cho từng cấu hình. A/Q16 mức 1 dù có con số 150 mét vì thiếu điều kiện và phần bật đèn; B/Q20 mức 0 vì chỉ có thông tin giấy phép trong Chương IV. Các mức còn lại có lý do cụ thể trong `ai_grounding.csv`. Đây là **độ đủ bằng chứng retrieval**, không có LLM sinh câu trả lời và không gọi là độ chính xác trả lời chatbot.
5. **Impact/tài nguyên:** A có thêm overlap và nhiều chunk, hữu ích dev Hit@3 nhưng làm vỡ điều kiện, đọc khó; B tăng Hit@1 dev, giảm lượng token/chunk nhưng có thể làm loãng ngữ nghĩa. C không thêm chi phí document embedding, cải thiện tuân thủ phạm vi; không sửa được nội dung bị cắt hoặc thứ hạng trong cùng chương. Thời gian query chỉ lưu như minh chứng, không xem là benchmark hiệu năng nghiêm ngặt vì query order/caching/HNSW warmup khác nhau và chỉ một lần chạy.

## 5. Hai ví dụ lỗi có thể truy lại

- **A/Q16**, phần 2 trang 2, Điều 25 khoản 2: top-2 chứa khoảng cách 150 mét nhưng bắt đầu ở đuôi từ “cấp”, mất điều kiện không vào được làn dừng khẩn cấp và phần bật đèn. Strict Evidence Hit@3=0, grounding AI=1; đây là lỗi biên chunk dù cùng trang gold. B/C rank 3 giữ được cả khoản và đạt hit. Xem `traces_test.jsonl`, question_id Q16.
- **B/Q20**, gold phần 2 trang 58, Điều 89 khoản 1, Chương IX: top-3 lại là trang 33/32/37 Chương IV nói hết điểm, hiệu lực/giấy phép quốc tế và cấp đổi. Không đủ trả lời quy định chuyển tiếp. C nhận filter IX từ câu hỏi nên lấy đúng Điều 89 ở rank 2; Hit@1 vẫn 0 vì rank 1 là Điều 88. Xem cùng trace, question_id Q20. Không đổi chiến lược đã chọn sau khi thấy lỗi test.

## 6. Kết luận, giới hạn và phần học viên cần chốt

Giữ **A** là lựa chọn chính thức theo quy tắc dev đã khóa, dù C có kết quả test cao hơn. Với nhu cầu demo lọc theo chương có thể minh họa C, nhưng không chọn lại bằng test. Hướng cải tiến cho **một thí nghiệm mới**: chunk theo Điều kèm tiêu đề, xử lý khoản nối qua trang với page_start/page_end, bỏ chữ ký số sau xác minh, bổ sung benchmark lớn hơn theo chủ đề/tài liệu và so sánh riêng từng size/overlap. Không áp dụng các cải tiến này rồi tiếp tục gọi 5 câu đã xem là test độc lập.

Giới hạn: một luật gốc, không gồm mức phạt/nghị định và không cập nhật pháp luật tự động; dấu chữ ký số còn lẫn ở trang đầu, đã phát hiện lúc review sau test nên giữ snapshot và ghi nhận; 20 câu do AI hỗ trợ soạn, chưa có người kiểm chứng độc lập; thang điểm định tính có thiên lệch; metadata đúng không đồng nghĩa evidence đủ. Không có API key, vector ngẫu nhiên hay TF-IDF thay embedding. Synthetic vectors chỉ xuất hiện trong unit test adapter Chroma, tách khỏi benchmark thật.

Tái lập: xem [README](../../README.md) và `starter/README.md`; dependencies/model revision được pin, `results/run/environment.json` lưu phiên bản thực tế. **9 kiểm thử đã chạy đạt** trong `results/tests.xml`; kiểm tra consistency ghi `results/verification.json` (60 truy vấn, 180 hits, freeze/chọn dev trước test, B/C không filter giống nhau, count nạp lại giữ nguyên). Test cơ sở dữ liệu cũng kiểm tra filter, lưu bền và xóa chunk cũ. Đã chạy lại toàn pipeline vào một index mới, dùng cache embedding: chunk dumps, dev/test metrics và lựa chọn A giống lần gốc; `results/reproduction_check.json` lưu đối chiếu. Đây là tái lập sau khi đã xem test, không điều chỉnh và không gọi là holdout mới. Số đo thời gian lần đầu vẫn được giữ riêng.

**AI hỗ trợ:** Codex đọc yêu cầu, viết code, tìm nguồn, soạn benchmark, chạy model thật, đo số liệu và đề xuất nhãn audit. Không có nhãn AI nào được ký thay học viên. Học viên cần đọc 3 phiếu `manual_*.csv` (30 coherence, 15 grounding, 45 metadata), sửa/điền nhãn và lý do sau đối chiếu nguồn, ghi người chấm thật và `human_verified`; chạy `summarize_manual.py`, cập nhật bảng human audit và giới hạn thiên lệch. Sau đó xác nhận thông tin cá nhân, tạo commit chốt, kiểm tra quyền truy cập repo và nộp link theo kênh lớp. **Không đánh dấu bài đã nộp hoặc audit đã hoàn thành khi chưa có bằng chứng.**
'''
    report=apply_confirmed_review(report,prefix='../../')
    path=ROOT/'report/individual/2A202603479_PhamTrungKien.md'
    path.write_text(report,encoding='utf-8')
    results_text='# Kết quả chạy thật\n\n'+table+'\n## Audit AI nháp — chưa được học viên chấm thủ công\n\n'+audit_table+'\nLựa chọn từ dev: A. Nhãn human audit còn pending; xem results/audit/README.md.\n\nRà soát AI bổ sung: A/P04 đổi 0 → 1 do còn hiểu được một phần; xem [lịch sử sửa nhãn](audit/review_corrections.json). Evidence được đối chiếu trực tiếp PDF ở [EVIDENCE_REVIEW.md](audit/EVIDENCE_REVIEW.md), mẫu audit ở [AUDIT_REVIEW.md](audit/AUDIT_REVIEW.md). Không thay số liệu retrieval.\n'
    if confirmed_summary():
        results_text=results_text.replace('## Audit AI nháp — chưa được học viên chấm thủ công',
            '## Audit đã được học viên xác nhận — có AI hỗ trợ').replace(
            'Lựa chọn từ dev: A. Nhãn human audit còn pending; xem results/audit/README.md.',
            'Lựa chọn từ dev: A. Phạm Trung Kiên xác nhận đã đối chiếu 20 câu và đủ 90 mẫu, đồng ý các đề xuất. Nhãn AI ban đầu được giữ riêng; đây không phải đánh giá mù. Xem [bản ghi xác nhận](audit/human_confirmation.json) và [manual_summary.json](audit/manual_summary.json).')
    (ROOT/'results/RESULTS.md').write_text(apply_confirmed_review(results_text,prefix='../'),encoding='utf-8')
    fields=['strategy','chunking','chunk_size','overlap','metadata','filter','vectorizer','hypothesis',
            'dev_hit1','dev_hit3','test_hit1','test_hit3','chunk_count','ingest_seconds','api_cost_usd','notes']
    config=read(ROOT/'starter/config.json')
    with (ROOT/'artifacts/experiment_log.csv').open('w',encoding='utf-8-sig',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=fields)
        writer.writeheader()
        for strategy in 'ABC':
            d=next(r for r in dev if r['strategy']==strategy)
            t=next(r for r in test if r['strategy']==strategy)
            spec=config['strategies'][strategy]
            writer.writerow({'strategy':strategy,'chunking':spec['chunking'],
                'chunk_size':spec.get('size',spec.get('max_size')),'overlap':spec['overlap'],
                'metadata':'document_id;source;page;section;law_id;version;language;printed_page;char_start;char_end',
                'filter':'section from question only' if strategy=='C' else 'none',
                'vectorizer':config['model_name']+'@'+config['model_revision'],
                'hypothesis':config['hypotheses'][strategy],
                'dev_hit1':f"{d['hit1_count']}/{d['n']}",'dev_hit3':f"{d['hit3_count']}/{d['n']}",
                'test_hit1':f"{t['hit1_count']}/{t['n']}",'test_hit3':f"{t['hit3_count']}/{t['n']}",
                'chunk_count':stats[strategy]['chunk_count'],'ingest_seconds':stats[strategy]['ingest_seconds'],
                'api_cost_usd':0,'notes':('Chosen on dev before test; ' if strategy=='A' else
                ('Shares B index; no extra document embedding; ' if strategy=='C' else ''))+
                ('Human audit verified; AI-assisted drafts accepted by student after source review' if confirmed_summary() else 'Human audit pending')})
    print('Report, measured tables and experiment log written')


if __name__=='__main__':
    main()
