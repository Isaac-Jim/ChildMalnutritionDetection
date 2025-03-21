import streamlit as st
import joblib
import numpy as np
import tensorflow as tf


model = joblib.load("malnutrition_log_model.joblib")


# Define mappings
parental_education_mapping = {"Primary": 0, "Secondary": 1, "Tertiary": 2}
market_access_mapping = {"Yes": 1, "No": 0}

# Location options (one-hot encoded)
locations = ["Homa Bay", "Kakamega", "Kisumu", "Migori", "Narok", "Siaya"]

st.title("Malnutrition Risk Prediction")
st.write("Enter the details below to predict the malnutrition risk.")

# User input fields
birth_order = st.number_input("Birth Order", min_value=1, step=1)
weight_for_age = st.number_input("Weight-for-Age", min_value=0.0, step=0.1)
parental_education = st.selectbox("Parental Education", ["Primary", "Secondary", "Tertiary"])
frequency_of_meals = st.number_input("Meals Per Day", min_value=1, step=1)
dietary_diversity = st.number_input("Dietary Diversity Score", min_value=0, step=1)
access_to_healthcare = st.selectbox("Access to Healthcare", ["Yes", "No"])
clean_water = st.selectbox("Access to Clean Water", ["Yes", "No"])
sanitation_facilities = st.selectbox("Sanitation Facilities", ["Yes", "No"])
availability_of_food = st.selectbox("Availability of Food", ["Yes", "No"])
seasonal_variations = st.selectbox("Seasonal Variations", ["Yes", "No"])
market_access = st.selectbox("Market Access", ["Yes", "No"])
location = st.selectbox("Location", locations)

# Encode categorical variables
parental_education = parental_education_mapping[parental_education]
market_access = market_access_mapping[market_access]
access_to_healthcare = 1 if access_to_healthcare == "Yes" else 0
clean_water = 1 if clean_water == "Yes" else 0
sanitation_facilities = 1 if sanitation_facilities == "Yes" else 0
availability_of_food = 1 if availability_of_food == "Yes" else 0
seasonal_variations = 1 if seasonal_variations == "Yes" else 0

# One-hot encoding for location
location_encoded = [1 if loc == location else 0 for loc in locations]

# Collect inputs into an array
input_data = np.array([[
    birth_order, weight_for_age, parental_education, frequency_of_meals,
    dietary_diversity, access_to_healthcare, clean_water, sanitation_facilities,
    availability_of_food, seasonal_variations, market_access, *location_encoded
]])

# Prediction button
if st.button("Predict Malnutrition Risk"):
    prediction = model.predict(input_data)
    predicted_class = int(np.argmax(prediction))  # Ensure correct class extraction
    risk_levels = {0: "Low", 1: "Moderate", 2: "High"}
    st.write(f"Predicted Malnutrition Risk: **{risk_levels[predicted_class]}**")
