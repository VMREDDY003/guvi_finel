# utils/prediction.py

import tensorflow as tf
from utils.preprocessing import load_and_prepare_image
import numpy as np

MODEL_PATH = "model/pneumonia_mobilenetv2.h5"

# Load model once to reuse
model = tf.keras.models.load_model(MODEL_PATH)

def predict_image(image_path):
    """
    Predicts if the X-ray image is Pneumonia or Normal.

    Args:
        image_path (str): Path to the image.

    Returns:
        dict: {'label': 'PNEUMONIA' or 'NORMAL', 'confidence': float probability}
    """
    img = load_and_prepare_image(image_path)
    pred = model.predict(img)[0][0]
    label = "PNEUMONIA" if pred > 0.5 else "NORMAL"
    confidence = float(pred if pred > 0.5 else 1 - pred)
    return {"label": label, "confidence": confidence}
