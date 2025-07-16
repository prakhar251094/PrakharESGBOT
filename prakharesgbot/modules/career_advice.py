import streamlit as st

def run_career_module():
    st.header("🧑‍💼 ESG Career Advisor")
    st.write("Get guidance based on your current certifications and goals.")

    finance = st.checkbox("✔️ MBA in Finance")
    cfa = st.checkbox("✔️ CFA ESG / CFA Level 1+")
    circular = st.checkbox("✔️ Circular Economy Certificate")
    esg_exp = st.slider("Years of ESG experience", 0, 10, 2)
    target_salary = st.selectbox("Your Target Salary", ["₹15–20 LPA", "₹20–35 LPA", "₹35+ LPA"])

    st.markdown("### 📈 Your Suggested Roadmap")

    if finance and circular:
        st.write("• ✅ Highlight your MBA + Circular blend — useful for ESG finance roles.")
        st.write("• 📚 Suggested Certifications: CFA ESG, SCR (GARP), FMVA, FSA, EU Taxonomy, GRI")
        st.write("• 💼 Focus: ESG analyst roles in green finance, infra, reporting.")
    if target_salary == "₹35+ LPA":
        st.write("• 🧠 Add AI + Carbon expertise for C-suite level roles by 2026.")
