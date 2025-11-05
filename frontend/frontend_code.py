import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MultiLabelBinarizer
import joblib

# -------------------------------------------------
# 1️⃣ Load trained model and preprocessing tools
# -------------------------------------------------
st.title("🩺 Medical Symptom Chatbot")
st.write("Describe your symptoms, and I’ll predict the most likely disease.")

# Load your trained model
model = load_model("medical_nn_model.h5")

# Load symptom encoder (you should have saved this during training)
# Example: joblib.dump(symptom_encoder, 'symptom_encoder.pkl')
try:
    symptom_encoder = joblib.load("symptom_encoder.pkl")
    disease_encoder = joblib.load("disease_encoder.pkl")
    st.success("Model and encoders loaded successfully.")
except:
    st.warning("⚠️ Could not find encoders. Make sure 'symptom_encoder.pkl' and 'disease_encoder.pkl' exist.")

# -------------------------------------------------
# 2️⃣ Chat Input
# -------------------------------------------------
user_input = st.chat_input("Describe your symptoms (e.g., fever, cough, sore throat)")

if user_input:
    st.chat_message("user").write(user_input)

    # -------------------------------------------------
    # 3️⃣ Preprocess Input
    # -------------------------------------------------
    # Split symptoms by commas
    symptoms = [s.strip().lower() for s in user_input.split(",")]

    try:
        # Convert symptoms to binary input vector
        X_input = symptom_encoder.transform([symptoms])

        # -------------------------------------------------
        # 4️⃣ Predict Disease
        # -------------------------------------------------
        prediction = model.predict(X_input)
        predicted_disease = disease_encoder.inverse_transform(prediction > 0.5)[0]

        # -------------------------------------------------
        # 5️⃣ Display Result
        # -------------------------------------------------
        bot_msg = f"🧠 Based on your symptoms, the possible disease could be: **{', '.join(predicted_disease)}**."
        st.chat_message("assistant").write(bot_msg)

    except Exception as e:
        st.chat_message("assistant").write(
            "⚠️ Sorry, I couldn’t process your symptoms. Please make sure they are valid."
        )
        st.error(str(e))
