import streamlit as st
import joblib
import numpy as np
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model
model_path = os.path.join(BASE_DIR, "models", "house_price_model.pkl")
model = joblib.load(model_path)

st.title("🏠 House Price Prediction")

st.write("Enter house details to predict price")

bedrooms = st.number_input("Bedrooms", min_value=0)
bathrooms = st.number_input("Bathrooms", min_value=0)
sqft_living = st.number_input("Living Area (sqft)", min_value=0)
sqft_lot = st.number_input("Lot Size (sqft)", min_value=0)
floors = st.number_input("Floors", min_value=0)
condition = st.number_input("Condition (1-5)", min_value=1, max_value=5)
sqft_above = st.number_input("Sqft Above", min_value=0)
sqft_basement = st.number_input("Sqft Basement", min_value=0)
yr_built = st.number_input("Year Built", min_value=1900)

if st.button("Predict Price"):

    features = np.array([[bedrooms, bathrooms, sqft_living,
                          sqft_lot, floors, condition,
                          sqft_above, sqft_basement, yr_built]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: Rs{prediction[0]:,.2f}")