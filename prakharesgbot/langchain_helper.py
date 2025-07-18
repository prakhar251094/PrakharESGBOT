def load_pdf_qa_chain(openai_api_key):
    import streamlit as st
    import random
    from PyPDF2 import PdfReader
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.vectorstores import FAISS
    from langchain.chains import RetrievalQA
    from langchain.chat_models import ChatOpenAI

    st.header("📚 Ask Questions from Uploaded ESG Frameworks")
    uploaded_files = st.file_uploader("Upload ESG PDFs", type=["pdf"], accept_multiple_files=True)
    wisdom = st.checkbox("Enable Wisdom Mode 🌱")

    if uploaded_files:
        text = ""
        for file in uploaded_files:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_text(text)

        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=openai_api_key)
        qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

        query = st.text_input("Ask your ESG question")
        if query:
            result = qa.run(query)
            st.markdown("### 🤖 ESG Answer")
            st.write(result)

            if wisdom:
                quotes = [
                    "“You have the right to work, not to the fruits of work.” — Bhagavad Gita",
                    "“Nature provides for every need, not every greed.” — Mahatma Gandhi",
                    "“Act without attachment to results.” — Gita 2.47"
                ]
                st.info(random.choice(quotes))
