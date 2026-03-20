import streamlit as st
import pickle
import numpy as np

st.title("🚖 Taxi Fare Prediction App")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.header("Enter Trip Details")
distance = st.number_input("Distance (km)", min_value=0.0)
passengers = st.number_input("Passengers", min_value=1)

if st.button("Predict Fare"):
    st.warning("This app was designed for fare prediction, but the trained model predicts taxi 'color' based on text features. Adjusting input for current model...")

    text_input = st.text_input("Enter pickup zone, dropoff zone, pickup borough, dropoff borough (e.g., 'Lenox Hill West UN/Turtle Bay South Manhattan Manhattan')")

    if text_input and st.button("Predict Taxi Color"):
       
        clean_text_input = clean_text(text_input)
        input_vec = vectorizer.transform([clean_text_input])
        predicted_color = model.predict(input_vec)[0]
        st.success(f"Predicted Taxi Color: {predicted_color}")
