import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Core carbon credit analysis logic
def carbon_credit_analysis(description, area, years, carbon_price=10, registry="Verra"):
    sequestration_rate = 10  # tCO2e per hectare per year
    estimated_credits = area * years * sequestration_rate
    revenue = estimated_credits * carbon_price

    project_type = "Afforestation / Reforestation"
    registry_info = {
        "Verra": "Likely fits Verra VCS methodologies (e.g., VM0015, VM0047)",
        "Gold Standard": "Likely fits Gold Standard Agriculture Forestry or Land Use (AFOLU)",
        "ART TREES": "Suitable for jurisdictional REDD+ under ART TREES",
        "CDM": "Applicable under AR methodologies of Clean Development Mechanism (CDM)"
    }.get(registry, "General carbon registry information")

    mrv_checklist = {
        "Baseline Scenario Defined": True,
        "Monitoring Plan Ready": True,
        "Leakage Considered": False,
        "Permanence Addressed": True
    }

    # Year-wise credit generation
    credits_per_year = [area * sequestration_rate for _ in range(years)]
    df = pd.DataFrame({
        "Year": list(range(1, years + 1)),
        "Credits": credits_per_year
    })

    return {
        "Project Type": project_type,
        "Estimated Credits (tCO2e)": estimated_credits,
        "Potential Revenue (USD)": revenue,
        "Registry Info": registry_info,
        "MRV Checklist": mrv_checklist,
        "Credits per Year Data": df
    }

# Streamlit UI
def run_carbon_module():
    st.header("🌳 Carbon Credit Estimator")

    description = st.text_input("Brief Project Description", "Bamboo agroforestry in Bihar")
    area = st.number_input("Project Area (in hectares)", min_value=1, value=1000)
    years = st.number_input("Project Duration (years)", min_value=1, value=10)
    price = st.slider("Carbon Price per ton (USD)", min_value=1, max_value=100, value=10)

    registry = st.selectbox("Choose Registry", ["Verra", "Gold Standard", "ART TREES", "CDM"])

    if st.button("Run Carbon Credit Analysis"):
        result = carbon_credit_analysis(description, area, years, carbon_price=price, registry=registry)

        st.markdown("### 🧾 Analysis Result")
        st.write(f"**Project Type:** {result['Project Type']}")
        st.write(f"**Estimated Credits:** {result['Estimated Credits (tCO2e)']:.0f} tCO₂e")
        st.write(f"**Potential Revenue:** ${result['Potential Revenue (USD)']:.2f}")
        st.write("**Registry Info:**", result['Registry Info'])

        st.markdown("### ✅ MRV Checklist")
        for k, v in result["MRV Checklist"].items():
            st.write(f"- {k}: {'✅' if v else '❌'}")

        st.markdown("### 📊 Estimated Credits by Year")
        df = result["Credits per Year Data"]
        st.line_chart(df.set_index("Year"))