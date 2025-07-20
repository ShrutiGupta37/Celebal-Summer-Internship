# app.py
import streamlit as st
import pickle
import numpy as np

# Load model
with open("week-7/titanic_model.pkl", 'rb') as f:
    model = pickle.load(f)

st.title("🚢 Titanic Survival Prediction")
st.write("Enter the passenger details to check the survival prediction:")

# User input
pclass = st.selectbox("Passenger Class (1 = Upper, 2 = Middle, 3 = Lower)", [1, 2, 3])
sex = st.selectbox("Sex", ["female", "male"])
age = st.slider("Age", 0, 100, 25)
fare = st.slider("Fare", 0.0, 600.0, 50.0)

# Encode sex
sex_encoded = 0 if sex == "female" else 1

# Prepare input
features = np.array([[pclass, sex_encoded, age, fare]])

# Predict
if st.button("Predict Survival"):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.success("🎉 The passenger **would have survived**.")
    else:
        st.error("😢 The passenger **would not have survived**.")
