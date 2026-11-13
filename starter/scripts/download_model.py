"""Only setup downloads from the network. Pipeline itself uses local files only."""
from pathlib import Path
import json
from huggingface_hub import snapshot_download

ROOT = Path(__file__).resolve().parents[2]
config = json.loads((ROOT / 'starter/config.json').read_text(encoding='utf-8'))
snapshot_download(config['model_name'], revision=config['model_revision'],
                  cache_dir=ROOT / 'artifacts/models/hub',
                  allow_patterns=['*.json', '*.safetensors', '*.txt', '1_Pooling/*'],
                  ignore_patterns=['onnx/*', 'openvino/*'])
print('Model downloaded and pinned:', config['model_revision'])
