
from src.generation import generate_answer
from src.ingestion import load_document as load_file
from src.chunking import chunk_documents
from src.embeddings import load_embedding_model, generate_embeddings
from src.vector_store import VectorStore


class RAGPipeline:
    def __init__(self):
        self.model = load_embedding_model()
        self.store = None

    def load_document(self, file_path):
        pages = load_file(file_path)

        # Convert TXT content into page-wise format.
        if isinstance(pages, str):
            pages = [{"page": 1, "text": pages}]

        chunks = chunk_documents(pages)

        for chunk in chunks:
            chunk["source"] = file_path

        embeddings = generate_embeddings(
            [chunk["text"] for chunk in chunks],
            self.model
        )

        self.store = VectorStore(embeddings.shape[1])
        self.store.add_chunks(chunks, embeddings)

    def retrieve(self, question, top_k=3):
        query_embedding = generate_embeddings(
            [question], self.model
        )[0]

        return self.store.search(query_embedding, top_k)

    def answer(self, question, results=None, top_k=3):
        if results is None:
            results = self.retrieve(question, top_k)

        evidence = "\n\n".join(
            f"Source: {r['chunk']['source']}, "
            f"Page: {r['chunk']['page']}\n"
            f"{r['chunk']['text']}"
            for r in results
        )

        return generate_answer(question, evidence)
