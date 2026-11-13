"""Persistent Chroma cosine HNSW collections; B and C share identical vectors."""
import math
from pathlib import Path
from typing import Any
import chromadb
from chromadb.config import Settings
from .models import Chunk

FILTER_FIELDS = {'section', 'law_id', 'version', 'language'}


class ChromaStore:
    def __init__(self, path: Path, dimensions: int, model_fingerprint: str) -> None:
        if dimensions < 1:
            raise ValueError('Invalid dimensions')
        self.dimensions = dimensions
        self.model_fingerprint = model_fingerprint
        self.client = chromadb.PersistentClient(path=str(path), settings=Settings(anonymized_telemetry=False))

    def collection(self, strategy: str):
        if strategy not in {'A', 'B', 'C'}:
            raise ValueError('Unknown strategy')
        name = 'traffic-fixed' if strategy == 'A' else 'traffic-paragraph'
        collection = self.client.get_or_create_collection(
            name, embedding_function=None,
            metadata={'model_fingerprint': self.model_fingerprint, 'dimensions': self.dimensions},
            configuration={'hnsw': {'space': 'cosine', 'ef_construction': 200,
                                    'ef_search': 100, 'num_threads': 1}})
        if collection.metadata.get('model_fingerprint') != self.model_fingerprint:
            raise ValueError('Index model/configuration changed; use a new store directory')
        return collection

    def _validate_vector(self, vector: list[float]) -> None:
        if len(vector) != self.dimensions or not all(math.isfinite(v) for v in vector):
            raise ValueError('Invalid vector dimensions/values')
        if not any(vector):
            raise ValueError('Zero vector')

    def upsert(self, strategy: str, chunks: list[Chunk], vectors: list[list[float]]) -> dict:
        if not chunks or len(chunks) != len(vectors):
            raise ValueError('Require equally sized nonempty chunks and vectors')
        for vector in vectors:
            self._validate_vector(vector)
        ids = [c.chunk_id for c in chunks]
        if len(set(ids)) != len(ids):
            raise ValueError('Duplicate chunk IDs')
        collection = self.collection(strategy)
        before = collection.count()
        for i in range(0, len(chunks), 128):
            batch = chunks[i:i+128]
            collection.upsert(ids=ids[i:i+128], embeddings=vectors[i:i+128],
                              documents=[c.text for c in batch],
                              metadatas=[dict(c.metadata) | {'document_id': c.document_id,
                                                            'source': c.source, 'page': c.page} for c in batch])
        # Full-corpus sync: delete obsolete IDs after successful writes. A series
        # of batches is not an atomic database transaction; rerun after failures.
        stale = sorted(set(collection.get(include=[])['ids']) - set(ids))
        for i in range(0, len(stale), 128):
            collection.delete(ids=stale[i:i+128])
        return {'before': before, 'after': collection.count(), 'removed_stale': len(stale)}

    def search(self, strategy: str, query_vector: list[float], top_k: int = 3,
               filters: dict[str, Any] | None = None) -> list[dict]:
        self._validate_vector(query_vector)
        if top_k < 1:
            raise ValueError('top_k must be positive')
        filters = filters or {}
        if set(filters) - FILTER_FIELDS or any(not isinstance(v, str) for v in filters.values()):
            raise ValueError('Unsupported metadata filter')
        conditions = [{k: {'$eq': v}} for k, v in sorted(filters.items())]
        where = {'$and': conditions} if len(conditions) > 1 else (conditions[0] if conditions else None)
        collection = self.collection(strategy)
        if not collection.count():
            raise RuntimeError('Empty index; run ingest first')
        result = collection.query(query_embeddings=[query_vector],
                                  n_results=min(top_k, collection.count()), where=where,
                                  include=['documents', 'metadatas', 'distances'])
        hits = [dict(chunk_id=i, text=t, score=1.0-d, metadata=m)
                for i,t,m,d in zip(result['ids'][0], result['documents'][0],
                                   result['metadatas'][0], result['distances'][0])]
        return sorted(hits, key=lambda h: (-h['score'], h['chunk_id']))
