def chunk_text(text, chunk_size=500, overlap=100):
    """Split text into overlapping chunks."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and smaller than chunk_size")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks

def chunk_documents(pages, chunk_size=500, overlap=100):
    """Chunk extracted pages while preserving page metadata."""
    all_chunks = []

    for page in pages:
        text = page["text"]
        chunks = chunk_text(text, chunk_size, overlap)

        for chunk in chunks:
           all_chunks.append({
            "text": chunk,
            "page": page["page"],
            "source": "sample.pdf"
})

    return all_chunks