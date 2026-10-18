import json
from src.generation import client, model_name


def verify_claim(claim, evidence):
    prompt = f"""
    You are a strict factual verification system.

    Verify the claim using ONLY the supplied evidence.

    CLAIM:
    {claim}

    EVIDENCE:
    {evidence}

    Classify the claim as exactly one of:

    SUPPORTED:
    Evidence directly supports the claim.

    CONTRADICTED:
    Evidence directly conflicts with the claim.

    INSUFFICIENT_EVIDENCE:
    Evidence does not provide enough information to decide.

    Do not assume that missing evidence means the claim is false.

    Return valid JSON only:
    {{
        "claim": "{claim}",
        "verdict": "SUPPORTED",
        "explanation": "Brief explanation based on evidence"
    }}
    """

    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config={"response_mime_type": "application/json"}
    )

    return json.loads(response.text)