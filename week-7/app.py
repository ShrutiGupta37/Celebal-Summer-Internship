# app.py

import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.datasets import load_iris

# Load the trained model and feature names

MODEL_PATH = 'iris_model.pkl'
FEATURES_PATH = 'features.pkl'

# Validate files
if not os.path.exists(MODEL_PATH):
    st.error(f"❌ Model file not found: {MODEL_PATH}")
    st.stop()

if not os.path.exists(FEATURES_PATH):
    st.error(f"❌ Features file not found: {FEATURES_PATH}")
    st.stop()

# Load model and features
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

with open(FEATURES_PATH, 'rb') as f:
    feature_names = pickle.load(f)


# Streamlit UI

st.set_page_config(page_title="Iris Classifier 🌸", layout="centered")

st.title("🌸 Iris Flower Prediction App")
st.write("Enter measurements below to predict the flower species using a trained machine learning model.")

# Sidebar for input features
st.sidebar.header("Input Features 🌿")
input_data = []
for feature in feature_names:
    val = st.sidebar.slider(f"{feature}", min_value=0.0, max_value=10.0, step=0.1)
    input_data.append(val)

# Predict on button click
if st.sidebar.button("🚀 Predict"):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    prediction_proba = model.predict_proba(input_array)

    species_name = load_iris().target_names[prediction]

    st.success(f"✅ Predicted Species: **{species_name}**")
    st.write("🔍 Prediction Probabilities:")
    st.bar_chart(prediction_proba[0])

# Visualizations


st.subheader("📊 Dataset Visualization")
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Series(iris.target).map(dict(enumerate(iris.target_names)))

# Plot pairplot with seaborn
with st.spinner("Generating visualizations..."):
    sns_plot = sns.pairplot(df, hue='species', corner=True)
    st.pyplot(sns_plot.fig)

# Footer
st.markdown("---")
st.caption("Created with ❤️ by Shruti Gupta during Celebal Internship - Week 7")
