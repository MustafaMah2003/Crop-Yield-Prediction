import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

model = joblib.load('crop_rf_model_minmax.pkl')
scaler = joblib.load('scaler_crop_minmax.pkl')

st.set_page_config(page_title="Crop Yield Predictor", layout="centered")
st.title("🌾 Crop Yield Prediction App")
st.subheader("📊Predict crop productivity based on environmental inputs")

st.sidebar.header("Enter Input Parameters")
st.sidebar.markdown("Adjust the sliders and select a crop to predict its yield.")
rainfall = st.sidebar.slider("Average Rainfall (mm/year)", 500, 2000, 1000, step=1)
temperature = st.sidebar.slider("Average Temperature (°C)", 10, 35, 25, step=1)
pesticide = st.sidebar.slider("Pesticide Used (tonnes)", 0, 80000, 121, step=1)
crop_type = st.sidebar.selectbox("Crop Type",['Cassava', 'Maize', 'Potatoes', 'Rice, paddy', 'Sorghum',
     'Soybeans', 'Sweet potatoes', 'Wheat'])

crop_list = ['Item_Cassava', 'Item_Maize', 'Item_Potatoes', 'Item_Rice, paddy', 'Item_Sorghum', 'Item_Soybeans', 'Item_Sweet potatoes', 'Item_Wheat']
crop_encoded = [1 if f"Item_{crop_type}" == item else 0 for item in crop_list]

input_data = [rainfall, pesticide, temperature] + crop_encoded

if st.button("Predict Crop Yield"):
    input_df = pd.DataFrame([input_data], columns=['average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp'] + crop_list)
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    st.success(f"🌾 Predicted Crop Yield: {int(prediction):,} hg/ha")

st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #f0f4f7, #d9e4f5);
        }
        .reportview-container {
            background-color: #f0f2f6;
            padding: 2rem;
        }
        .stButton>button {
            background-color: #008CBA;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1em;
            font-size: 1em;
        }
        .stButton>button:hover {
            background-color: #006f9a;
        }
        .stSidebar .sidebar-content {
            background-color: #ffffff;
        }
        .stSuccess {
            font-weight: bold;
            font-size: 1.2em;
            color: #2e8b57;
        }
    </style>
""", unsafe_allow_html=True)