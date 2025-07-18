import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings


def load_pdf_qa_chain(openai_api_key):
    st.subheader("📄 Upload ESG PDF Document")
    
    pdf = st.file_uploader("Upload a PDF", type="pdf")

    if pdf:
        # ✅ Save uploaded file to disk
        temp_path = os.path.join("temp", pdf.name)
        os.makedirs("temp", exist_ok=True)
        with open(temp_path, "wb") as f:
            f.write(pdf.read())

        # ✅ Load the saved file using PyPDFLoader
        loader = PyPDFLoader(temp_path)
        documents = loader.load()

        # ✅ Split text
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = splitter.split_documents(documents)

        # ✅ Vector store from text
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        vectorstore = FAISS.from_documents(texts, embeddings)

        # ✅ Chat model
        llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)

        # ✅ Retrieval QA chain
        chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            chain_type="stuff"
        )

        # ✅ Input box
        question = st.text_input("❓ Ask a question about the PDF:")
        if question:
            with st.spinner("Generating answer..."):
                result = chain.run(question)
                st.success("✅ Answer:")
                st.write(result)