import streamlit as st
import numpy as np
import joblib
import json

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AquaSense AI",
    page_icon="💧",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("water_quality_model.pkl")
imputer = joblib.load("imputer.pkl")

with open("features (2).json", "r") as f:
    features = json.load(f)

# -----------------------------
# Title
# -----------------------------
st.title("💧 AquaSense AI")
st.subheader("AI-Powered Water Potability Prediction")

st.write(
    "Enter the water quality parameters below to determine whether the water is safe for drinking."
)

st.divider()

# -----------------------------
# Input Fields
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    ph = st.number_input(
        "pH",
        min_value=0.0,
        max_value=14.0,
        value=7.0
    )

    hardness = st.number_input(
        "Hardness",
        min_value=0.0,
        value=200.0
    )

    solids = st.number_input(
        "Solids",
        min_value=0.0,
        value=15000.0
    )

    chloramines = st.number_input(
        "Chloramines",
        min_value=0.0,
        value=7.0
    )

    sulfate = st.number_input(
        "Sulfate",
        min_value=0.0,
        value=330.0
    )

with col2:

    conductivity = st.number_input(
        "Conductivity",
        min_value=0.0,
        value=425.0
    )

    organic_carbon = st.number_input(
        "Organic Carbon",
        min_value=0.0,
        value=14.0
    )

    trihalomethanes = st.number_input(
        "Trihalomethanes",
        min_value=0.0,
        value=66.0
    )

    turbidity = st.number_input(
        "Turbidity",
        min_value=0.0,
        value=4.0
    )

st.divider()

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Water Quality", use_container_width=True):

    input_data = np.array([[
        ph,
        hardness,
        solids,
        chloramines,
        sulfate,
        conductivity,
        organic_carbon,
        trihalomethanes,
        turbidity
    ]])

    input_data = imputer.transform(input_data)

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    confidence = probability[prediction] * 100

    st.subheader("Prediction")

    if prediction == 1:

        st.success("Water is Safe for Drinking")

    else:

        st.error("Water is Not Safe for Drinking")

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )

    st.progress(confidence / 100)
