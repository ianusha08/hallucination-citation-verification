from src.rag import RAGPipeline
from src.claim_extraction import extract_claims
from src.verification import verify_claim


class HallucinationDetector:

    def __init__(self):
        self.rag = RAGPipeline()

    def load_document(self, file_path):
        self.rag.load_document(file_path)

    def analyze(self, question):
        # Retrieve evidence and generate an answer
        results = self.rag.retrieve(question)

        answer = self.rag.answer(question, results=results)
        # Extract individual factual claims
        claims = extract_claims(answer)

        # Prepare retrieved evidence
        evidence = "\n\n".join(
            result["chunk"]["text"] for result in results
        )

        # Verify every claim
        verification_results = []

        for claim in claims:
            result = verify_claim(claim, evidence)
            verification_results.append(result)

        return {
            "question": question,
            "answer": answer,
            "claims": verification_results
        }