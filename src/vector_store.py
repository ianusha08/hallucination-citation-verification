import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks = []

    def add_chunks(self, chunks, embeddings):
        embeddings = np.asarray(embeddings, dtype="float32")

        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def search(self, query_embedding, top_k=3):
        query_embedding = np.asarray(
            [query_embedding], dtype="float32"
        )

        distances, indices = self.index.search(query_embedding, top_k)

        results = []

        for distance, index in zip(distances[0], indices[0]):
            if index != -1:
                results.append({
                    "chunk": self.chunks[index],
                    "distance": float(distance)
                })

        return results