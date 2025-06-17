# 🚑 Pneumonia Detection from Chest X-Ray Images using CNN

![Pneumonia Detection](pneumonia-Detection-from-Chest-X-Ray.png)  
*Detect Pneumonia with Deep Learning on Chest X-rays*

---

[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![TensorFlow](https://img.shields.io/badge/tensorflow-2.x-orange?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)  
[![Streamlit](https://img.shields.io/badge/streamlit-app-red?logo=streamlit&logoColor=white)](https://streamlit.io/)  

---

## 🌟 Project Overview

Early and accurate detection of **pneumonia** is critical in saving lives. This project implements a **Convolutional Neural Network (CNN)** leveraging the power of **MobileNetV2** to classify chest X-ray images into **pneumonia** or **normal** categories.

This automated approach aims to assist radiologists and healthcare providers by reducing diagnosis time and improving accuracy.

---

## 🛠️ Features

- 🔍 **Image preprocessing:** Clean, normalize, and augment chest X-ray images for better model training.  
- 🤖 **Deep learning model:** MobileNetV2 based CNN optimized for accuracy and speed.  
- ⚖️ **Handles data imbalance:** Uses class weighting and early stopping to improve model performance.  
- 📊 **Evaluation:** Provides accuracy, confusion matrix, and loss curves for model insights.  
- 🚀 **Streamlit web app:** User-friendly interface for image upload and real-time pneumonia prediction.  

---

## 📁 Dataset

We use the **Chest X-Ray Images (Pneumonia)** dataset from Kaggle:

[Kaggle Dataset Link](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

---

## 💻 Installation

1. **Clone this repository**

   ```
   git clone https://github.com/VMREDDY003/Pneumonia-Detection-from-Chest-X-Ray-Images.git
   cd Pneumonia-Detection-from-Chest-X-Ray-Images
---

## Create and activate a virtual environment

 
      python3 -m venv .venv
      source .venv/bin/activate   # Windows: .venv\Scripts\activate
---

## Install dependencies
    
      pip install -r requirements.txt
---

## 🚀 Usage
Run the Streamlit Web Application

      streamlit run app/app.py

Open the displayed URL (usually http://localhost:8501) in your browser. Upload a chest X-ray image to get an instant pneumonia prediction!

## 🏋️‍♂️ Model Training
To retrain or fine-tune the model:

Prepare your dataset in the data/ folder.

### Run the training notebook:

      jupyter notebook notebooks/eda_and_training.ipynb
or run the training script:

      python scripts/train_model.py
Model weights will be saved in the model/ directory as pneumonia_mobilenetv2.h5.

## 🗂️ Project Structure

      Pneumonia-Detection-from-Chest-X-Ray-Images/
      │
      ├── app/                     # Streamlit application files
      ├── data/                    # Dataset (not included in repo)
      ├── model/                   # Saved model weights
      ├── notebooks/               # Exploratory Data Analysis & training notebooks
      ├── scripts/                 # Training and utility scripts
      ├── utils/                   # Helper functions (prediction, preprocessing)
      ├── requirements.txt         # Project dependencies
      └── README.md                # Project documentation

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check issues page.

📬 Contact
VM Reddy  
Reach out at: [malleswarareddy8008@gmail.com]

