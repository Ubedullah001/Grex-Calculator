import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Grex Yarn Count Calculator",
    page_icon="🧵",
    layout="centered"
)

# Title
st.title("🧵 Grex (Tex) Yarn Count Calculator")
st.write("Calculate yarn count in the Grex/Tex system.")

st.divider()

# Input
weight = st.number_input(
    "Enter yarn weight (grams):",
    min_value=0.0,
    value=1.0,
    step=0.1
)

length = st.number_input(
    "Enter yarn length (meters):",
    min_value=0.0,
    value=1000.0,
    step=10.0
)

# Calculate button
if st.button("Calculate Yarn Count"):
    if weight > 0 and length > 0:
        # Tex formula:
        # Tex = Weight in grams × 1000 / Length in meters
        tex = (weight * 1000) / length

        # Grex formula:
        # Grex = Weight in grams × 10000 / Length in meters
        grex = (weight * 10000) / length

        st.success("Calculation completed!")

        st.metric("Yarn Count (Tex)", f"{tex:.2f} Tex")
        st.metric("Yarn Count (Grex)", f"{grex:.2f} Grex")

        st.info(
            "Formula: Grex = (Weight in grams × 10,000) ÷ Length in meters"
        )

    else:
        st.error("Please enter values greater than zero.")

st.divider()

st.caption("Textile Yarn Count Calculator | Made with Streamlit")
