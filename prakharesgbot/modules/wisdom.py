import streamlit as st
import random

def show_wisdom():
    st.header("🧘 ESG Wisdom Mode")
    quotes = [
        "“Act without expectation.” — Bhagavad Gita",
        "“The earth has enough for everyone's need, not greed.” — Gandhi",
        "“Silence is the sleep that nourishes wisdom.” — Bacon",
        "“Karma is not punishment, but a mirror of actions.” — Upanishads",
    ]
    st.info(random.choice(quotes))
