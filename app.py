
import streamlit as st
from src.pipeline import HallucinationDetector

st.set_page_config(
    page_title="Hallucination Detection Framework",
    page_icon="🔍",
    layout="wide"
)

st.title("Hallucination & Citation Verification Framework")
st.write("Upload a document and ask questions. The system will verify generated answers against document evidence.")

uploaded_file = st.file_uploader(
    "Upload a PDF or TXT document",
    type=["pdf", "txt"]
)

question = st.text_input("Ask a question about your document")

if st.button("Analyze"):
    if uploaded_file is None:
        st.warning("Please upload a document first.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Analyzing your question..."):
            try:
                detector = HallucinationDetector()

                file_path = f"data/raw/{uploaded_file.name}"
                with open(file_path, "wb") as file:
                    file.write(uploaded_file.getbuffer())

                detector.load_document(file_path)
                result = detector.analyze(question)

                st.subheader("Generated Answer")
                st.write(result["answer"])

                st.subheader("Claim Verification")
                for item in result["claims"]:
                    st.markdown(f"**Claim:** {item['claim']}")
                    st.write(f"**Verdict:** {item['verdict']}")
                    st.write(f"**Explanation:** {item['explanation']}")
                    st.divider()

            except Exception as error:
                st.error(f"An error occurred: {error}")
