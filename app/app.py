# app/app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from PIL import Image
import numpy as np
from utils.prediction import predict_image


st.set_page_config(page_title="Pneumonia Detection from Chest X-Rays", layout="centered")

st.title("🩺 Pneumonia Detection from Chest X-Ray Images")
st.write(
    """
    Upload a chest X-ray image, and the AI model will predict if the lungs are **Normal** or have **Pneumonia**.
    
    This app uses a CNN model trained on Kaggle's Chest X-Ray dataset.
    """
)

uploaded_file = st.file_uploader("Choose a chest X-ray image (JPEG/PNG)", type=["jpeg", "jpg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded X-Ray", use_container_width=True)
    
    # Save temp file to pass path to prediction utils
    temp_path = "temp_uploaded_image.jpg"
    image.save(temp_path)
    
    with st.spinner("Analyzing..."):
        result = predict_image(temp_path)
    
    st.markdown("---")
    st.subheader("Prediction Results:")
    label = result['label']
    confidence = result['confidence'] * 100
    
    if label == "PNEUMONIA":
        st.error(f"⚠️ Pneumonia detected with {confidence:.2f}% confidence.")
    else:
        st.success(f"✅ Lungs are Normal with {confidence:.2f}% confidence.")
    
    st.markdown(
        """
        ---
        **Note:** This tool is for research and educational purposes only. Always consult a medical professional for diagnosis.
        """
    )
