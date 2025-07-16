import streamlit as st

def run_carbon_module():
    st.header("🌳 Carbon Credit Estimator")
    st.write("Estimate carbon credit yield from reforestation / REDD+ projects")

    area = st.number_input("Project Area (in hectares)", min_value=1, value=1000)
    years = st.number_input("Project Duration (years)", min_value=1, value=10)
    methodology = st.selectbox("Methodology", ["REDD+", "Afforestation", "Agroforestry"])
    
    if methodology == "REDD+":
        credits_per_hectare = 8
    elif methodology == "Afforestation":
        credits_per_hectare = 12
    else:
        credits_per_hectare = 6

    total_credits = area * credits_per_hectare * (years / 10)
    st.success(f"Estimated Carbon Credits: {total_credits:,.0f} tCO₂e")
