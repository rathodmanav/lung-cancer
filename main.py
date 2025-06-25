# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:40:00 2025

@author: Yash
"""

import pickle
import streamlit as st

# Load the model
lung_cancer_model = pickle.load(open("C:/Users/Yash/OneDrive/Desktop/lung cancer/lung_cancer.sav", 'rb'))

# Streamlit app title
st.title("Lung Cancer Survival Prediction App")

st.markdown(
    """
    ### Predict whether a person will survive lung cancer based on their medical and lifestyle details.
    """
)

# Input fields
age = st.number_input("Age:", min_value=0, max_value=100, value=50)
gender = st.selectbox("Gender:", ["Male", "Female"])
country = st.selectbox("Country:", [
    "Malta", "Ireland", "Portugal", "France", "Croatia", "Greece", "Spain", 
    "Netherlands", "Denmark", "Slovenia", "Belgium", "Hungary", "Romania", 
    "Poland", "Italy", "Germany", "Estonia", "Czech Republic", "Lithuania", 
    "Slovakia", "Austria", "Finland", "Luxembourg", "Cyprus", "Latvia", "Bulgaria"
])
stage = st.selectbox("Cancer Stage:", ["Stage 1", "Stage 2", "Stage 3", "Stage 4"])
family_history = st.selectbox("Family History:", ["Yes", "No"])
smoking_status = st.selectbox("Smoking Status:", ["Passive Smoker", "Former Smoker", "Never Smoked", "Current Smoker"])
bmi = st.slider("BMI:", min_value=0.0, max_value=100.0, value=25.0, step=0.1)
cholesterol = st.number_input("Cholesterol Level:", min_value=0, max_value=500, value=200)
hypertension = st.selectbox("Hypertension:", ["Yes", "No"])
asthma = st.selectbox("Asthma:", ["Yes", "No"])
cirrhosis = st.selectbox("Cirrhosis:", ["Yes", "No"])
other_cancer = st.selectbox("Other Cancer:", ["Yes", "No"])
treatment_type = st.selectbox("Treatment Type:", ["Chemotherapy", "Surgery", "Combined", "Radiation", "Other"])

# Encode categorical inputs
country_encoded = {
    "Malta": 0, "Ireland": 1, "Portugal": 2, "France": 3, "Croatia": 4, 
    "Greece": 5, "Spain": 6, "Netherlands": 7, "Denmark": 8, "Slovenia": 9,
    "Belgium": 10, "Hungary": 11, "Romania": 12, "Poland": 13, "Italy": 14,
    "Germany": 15, "Estonia": 16, "Czech Republic": 17, "Lithuania": 18, 
    "Slovakia": 19, "Austria": 20, "Finland": 21, "Luxembourg": 22, "Cyprus": 23,
    "Latvia": 24, "Bulgaria": 25
}[country]
gender_encoded = 1 if gender == "Male" else 0
stage_encoded = {"Stage 1": 1, "Stage 2": 2, "Stage 3": 3, "Stage 4": 4}[stage]
family_history_encoded = 1 if family_history == "Yes" else 0
smoking_status_encoded = {
    "Passive Smoker": 0, "Former Smoker": 1, "Never Smoked": 2, "Current Smoker": 3
}[smoking_status]
hypertension_encoded = 1 if hypertension == "Yes" else 0
asthma_encoded = 1 if asthma == "Yes" else 0
cirrhosis_encoded = 1 if cirrhosis == "Yes" else 0
other_cancer_encoded = 1 if other_cancer == "Yes" else 0
treatment_type_encoded = {
    "Chemotherapy": 0, "Surgery": 1, "Combined": 2, "Radiation": 3, "Other": 4
}[treatment_type]

# Combine inputs into a list
input_data = [
    age, gender_encoded,country_encoded, stage_encoded, family_history_encoded, smoking_status_encoded,
    bmi, cholesterol, hypertension_encoded, asthma_encoded, cirrhosis_encoded,
    other_cancer_encoded, treatment_type_encoded
]

# Prediction
if st.button("Predict Survival Status"):
    try:
        prediction = lung_cancer_model.predict([input_data])[0]
        result = "Survived" if prediction == 1 else "Not Survived"
        st.success(f"Prediction: {result}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")

st.markdown(
    """
    **Note:** This prediction is based on historical data and may not guarantee outcomes.
    """
)
