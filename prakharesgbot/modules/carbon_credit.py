from prakharesgbot.carbon_credit import carbon_credit_analysis
description = st.text_input("Brief Project Description", "Bamboo agroforestry in Bihar")
area = st.number_input("Project Area (in hectares)", min_value=1, value=1000)
years = st.number_input("Project Duration (years)", min_value=1, value=10)

if st.button("Run Carbon Credit Analysis"):
    result = carbon_credit_analysis(description, area, years)
    
    st.markdown("### 🧾 Analysis Result")
    st.write(f"**Project Type:** {result['Project Type']}")
    st.write(f"**Estimated Credits:** {result['Estimated Credits (tCO2e)']:.0f} tCO₂e")
    st.write(f"**Potential Revenue:** ${result['Potential Revenue (USD)']:.2f}")
    st.write("**Registry Info:**", result['Registry Info'])
    
    st.markdown("### ✅ MRV Checklist")
    for k, v in result["MRV Checklist"].items():
        st.write(f"- {k}: {'✅' if v else '❌'}")
price = st.slider("Carbon Price per ton (USD)", min_value=1, max_value=100, value=10)
