"""Real, pinned Sentence Transformers model. No mock fallback at run time."""
from pathlib import Path
from typing import Protocol
import hashlib
import json
import numpy as np


class Embedder(Protocol):
    model_name: str
    dimensions: int

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Return one vector per input text, in the same order."""
        ...

    def embed_query(self, question: str) -> list[float]:
        """Return a query vector compatible with the stored document vectors."""
        ...


class MyEmbedder:
    def __init__(self, model_name: str, revision: str, cache_dir: Path) -> None:
        import torch
        from sentence_transformers import SentenceTransformer
        torch.set_num_threads(4)
        torch.manual_seed(42)
        self.model_name, self.revision = model_name, revision
        self.model = SentenceTransformer(model_name, revision=revision, device='cpu',
                                         cache_folder=str(cache_dir), local_files_only=True)
        self.dimensions = self.model.get_sentence_embedding_dimension()
        self.model.max_seq_length = 256

    def token_counts(self, texts: list[str]) -> list[int]:
        return [len(ids) for ids in self.model.tokenizer(texts, truncation=False,
                                                        verbose=False)['input_ids']]

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        vectors = self.model.encode(texts, batch_size=16, normalize_embeddings=True,
                                    show_progress_bar=False, convert_to_numpy=True)
        if not np.isfinite(vectors).all():
            raise ValueError('Non-finite model output')
        return vectors.tolist()

    def embed_query(self, question: str) -> list[float]:
        return self.embed_documents([question])[0]

    def cached_documents(self, texts: list[str], directory: Path) -> tuple[list[list[float]], bool]:
        key = hashlib.sha256(json.dumps([self.model_name, self.revision, 256, texts],
                                        ensure_ascii=False).encode('utf-8')).hexdigest()
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / f'{key}.npy'
        if path.exists():
            vectors = np.load(path, allow_pickle=False)
            if vectors.shape != (len(texts), self.dimensions) or not np.isfinite(vectors).all():
                raise ValueError('Invalid embedding cache')
            return vectors.tolist(), True
        vectors = self.embed_documents(texts)
        np.save(path, np.asarray(vectors, dtype=np.float32), allow_pickle=False)
        return vectors, False
