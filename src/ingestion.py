import pymupdf
from pathlib import Path


def extract_text_from_pdf(file_path):
    """Extract text from a PDF, page by page."""
    extracted_pages = []

    pdf = pymupdf.open(file_path)

    for page_number, page in enumerate(pdf, start=1):
        text = page.get_text()

        extracted_pages.append({
            "page": page_number,
            "text": text
        })

    pdf.close()
    return extracted_pages

def extract_text_from_txt(file_path):
    """Extract text from a TXT file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()



def load_document(file_path):
    """Load a PDF or TXT document."""
    file_path = str(file_path)

    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    elif file_path.lower().endswith(".txt"):
        return extract_text_from_txt(file_path)

    else:
        raise ValueError("Unsupported file format. Use PDF or TXT.")