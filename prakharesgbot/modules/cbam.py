import streamlit as st
import pandas as pd

def run_cbam_module():
    st.header("🏭 CBAM Impact Calculator")
    st.write("Estimate CBAM costs for Indian exporters under EU carbon border tax.")

    # Sample dataset
    data = {
        'Company': ['Tata Steel', 'JSW Steel', 'Adani Cement'],
        'EU Exports (tons)': [200000, 150000, 100000],
        'Emission Intensity (tCO2e/ton)': [2.1, 2.4, 0.8]
    }
    df = pd.DataFrame(data)

    st.dataframe(df)

    carbon_price = st.slider("EU Carbon Price (€/tCO2e)", min_value=50, max_value=120, value=90)
    selected_company = st.selectbox("Select a company", df['Company'])

    if selected_company:
        row = df[df['Company'] == selected_company].iloc[0]
        cbam_cost = row['EU Exports (tons)'] * row['Emission Intensity (tCO2e/ton)'] * carbon_price
        st.success(f"Estimated CBAM Cost: €{cbam_cost:,.2f}")
