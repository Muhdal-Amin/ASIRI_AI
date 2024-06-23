import streamlit as st # type: ignore
from dotenv import load_dotenv # type: ignore
from PyPDF2 import PdfReader # type: ignore

#function Prototypes

def get_pdf_text(pdf_docs):
    text =""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
    
# main - Code entry point
def main():
    load_dotenv()
    # Create Graphical User Interface.

    # Set Page Configs.
    st.set_page_config(page_title="ASIRI AI", page_icon=":sparkles:")

    st.header("Welcome To ASIRI AI :sparkles:")
    st.markdown("***")
    st.subheader("How Can I Help you Today?")
    st.text("")
    st.text_input("Ask a question :")

    # Create a Side Bar
    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDF files here", accept_multiple_files=True )
        if st.button("Run"):
            with st.spinner("Generating...."):
                
                # Get PDF Document text
                raw_text = get_pdf_text(pdf_docs)
            
    


if __name__ == "__main__":
    main()