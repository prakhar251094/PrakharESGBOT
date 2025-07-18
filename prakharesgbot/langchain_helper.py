from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
import streamlit as st


def load_pdf_qa_chain(openai_api_key):
    st.subheader("📄 Upload ESG PDF Document")
    
    pdf = st.file_uploader("Upload a PDF", type="pdf")

    if pdf:
        # Load the PDF
        loader = PyPDFLoader(pdf.name)
        with open(pdf.name, "wb") as f:
            f.write(pdf.read())

        documents = loader.load()

        # Split the text
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )
        texts = text_splitter.split_documents(documents)

        # Embed and index
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        vectorstore = FAISS.from_documents(texts, embeddings)

        # Set up LLM
        llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)

        # Create QA chain
        chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever()
        )

        # Ask a question
        question = st.text_input("❓ Ask a question about the document:")
        if question:
            with st.spinner("Thinking..."):
                result = chain.run(question)
                st.success("✅ Answer:")
                st.write(result)