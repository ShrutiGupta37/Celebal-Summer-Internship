# app.py
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the model and features
with open('iris_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('features.pkl', 'rb') as f:
    feature_names = pickle.load(f)

# Title
st.title("🌸 Iris Flower Prediction App")
st.write("Input flower features to predict its species.")

# Sidebar inputs
input_data = []
for feature in feature_names:
    val = st.sidebar.slider(f"{feature}", min_value=0.0, max_value=10.0, step=0.1)
    input_data.append(val)

# Predict
if st.sidebar.button("Predict"):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    prediction_proba = model.predict_proba(input_array)

    # Display results
    st.success(f"Predicted Species: {load_iris().target_names[prediction]}")
    st.write("Prediction Probabilities:")
    st.bar_chart(prediction_proba[0])

# Visualize dataset
st.subheader("📊 Data Distribution")
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Series(iris.target).map(dict(enumerate(iris.target_names)))

fig, ax = plt.subplots()
sns.pairplot(df, hue='species', corner=True)
st.pyplot(fig)
