import json
from src.generation import client, model_name


def extract_claims(answer):
    prompt = f"""
    Break the following answer into individual factual claims.

    Rules:
    - Each claim must express one independently verifiable fact.
    - Do not add information.
    - Ignore opinions and conversational filler.
    - Return only a valid JSON array of strings.

    Answer:
    {answer}
    """

    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    return json.loads(response.text)