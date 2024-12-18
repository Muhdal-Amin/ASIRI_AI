import streamlit as st 
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
#from langchain.embeddings import OpenAIEmbeddings
import torch
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from InstructorEmbedding import INSTRUCTOR
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI # type: ignore
from htmltemplates import css, bot_template, user_template
#from langchain_community.llms import HuggingFaceHub

#function Prototypes

# Function to get texts in Uploaded PDF files.
def get_pdf_text(pdf_docs):
    text =""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to split text into chunks.
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 5000, 
        chunk_overlap = 500,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create vector stores for embedded text chunks
def get_vector_store(text_chunks):
    #embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

# Function to create a conversation change
def get_conversation_chain(vectorstore):
    #llm = ChatOpenAI()
    llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(memory_keys = 'chat_history', return_message=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vectorstore.as_retriever(),
        memory = memory
    )
    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


# main - Code entry point
def main():
    load_dotenv()
    # Create Graphical User Interface.
 
    # Set Page Configs.
    st.set_page_config(page_title="ASIRI AI", page_icon=":sparkles:")

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Welcome To ASIRI AI :sparkles:")
    st.markdown("***")
    st.subheader("How Can I Help you Today?")
    st.text("")
    user_question = st.text_input("Ask a question :")
    if user_question:
        handle_userinput(user_question)

    # Create a Side Bar
    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDF files here", accept_multiple_files=True )
        if st.button("Run"):
            with st.spinner("Processing..."):
                
                # Get PDF Document text
                raw_text = get_pdf_text(pdf_docs)

                # Get splitted text chunks
                text_chunks = get_text_chunks(raw_text)

                # Creating Vector Store for text chunks
                vector_store = get_vector_store(text_chunks)

                # Creating a conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)
               
            
    


if __name__ == "__main__":
    main()