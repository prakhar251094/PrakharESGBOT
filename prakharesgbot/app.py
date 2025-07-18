import streamlit as st
import os
from dotenv import load_dotenv

from modules import cbam, carbon_credit, career_advice, wisdom
from langchain_helper import load_pdf_qa_chain

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="PrakharESGBot Universal", layout="wide")
st.title("🌿 PrakharESGBot Universal — ESG Wisdom, Finance & Impact")

st.sidebar.title("🧩 Choose a Module")
mode = st.sidebar.radio("📍 Select Function", [
    "📚 ESG Framework Q&A",
    "🏭 CBAM Company Impact",
    "🌳 Carbon Credit Estimator",
    "🧑‍💼 ESG Career Advice",
    "🧘 Wisdom Reflection"
])

if mode == "📚 ESG Framework Q&A":
    load_pdf_qa_chain(openai_api_key=openai_api_key)

elif mode == "🏭 CBAM Company Impact":
    cbam.run_cbam_module()

elif mode == "🌳 Carbon Credit Estimator":
    carbon_credit.run_carbon_module()

elif mode == "🧑‍💼 ESG Career Advice":
    career_advice.run_career_module()

elif mode == "🧘 Wisdom Reflection":
    wisdom.show_wisdom()
