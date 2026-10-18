def validate_citations(citations, retrieved_chunks):
    valid_citations = []

    for citation in citations:
        source = citation.get("source")
        page = citation.get("page")

        exists = any(
            chunk.get("source") == source
            and chunk.get("page") == page
            for chunk in retrieved_chunks
        )

        valid_citations.append({
            "source": source,
            "page": page,
            "valid": exists
        })

    return valid_citations