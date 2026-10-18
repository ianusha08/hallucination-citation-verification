import os
from dotenv import load_dotenv
import google.genai as genai


load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)


def generate_answer(question, evidence):
    prompt = f"""
    Answer the question using ONLY the evidence below.

    If the evidence is insufficient, say so.
    Do not invent facts.

    Evidence:
    {evidence}

    Question:
    {question}
    """

    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )

    return response.text