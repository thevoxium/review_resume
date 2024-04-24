import streamlit as st
import pdfplumber
from model import model_call


def main():
    st.title("Review Your Resume")

    # File uploader
    uploaded_file = st.file_uploader("upload", label_visibility = "hidden", type="pdf")

    if uploaded_file is not None:
        # Extract text from the PDF
        with pdfplumber.open(uploaded_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()

        
        job_role = st.text_input("Profile you are applying for..", "")
        if len (job_role) > 0:
            st.markdown(model_call(text, job_role), unsafe_allow_html = True)

if __name__ == "__main__":
    main()