# guvi_finel

# 📊 GUVI Final Projects Repository

Welcome to the **GUVI Final Projects** repository!  
This repository contains three comprehensive data science and machine learning projects, each organized in separate branches for clarity and modularity. These projects demonstrate end-to-end workflows — from data preprocessing and model development to visualization and deployment.

---

## 🗂 Repository Structure

Each project is located in a separate Git branch:

| Branch Name                  | Project Title                                             | Domain                      |
|-----------------------------|------------------------------------------------------------|-----------------------------|
| `pneumonia-detection`       | Pneumonia Detection from Chest X-Ray Images using CNN     | Computer Vision / Healthcare |
| `next-word-prediction`      | Next Word Prediction using LSTM                           | Natural Language Processing |
| `eda-superstore-analysis`   | Exploratory Data Analysis on Global Superstore Sales Data | Business Intelligence / EDA |

---

## 🚀 Project Summaries

### 🔬 1. Pneumonia Detection from Chest X-Ray Images using CNN

- **Objective:** Automatically detect pneumonia from X-ray images using deep learning.
- **Model:** MobileNetV2 CNN architecture.
- **Features:**
  - Data preprocessing and augmentation
  - Model training and evaluation with metrics
  - Streamlit-based frontend for image upload and prediction
- **Skills Used:** TensorFlow, Keras, OpenCV, Streamlit

---

### 🧠 2. Next Word Prediction using LSTM

- **Objective:** Predict the next word in a sequence using an LSTM language model.
- **Dataset:** WikiText-2 from Hugging Face Datasets.
- **Features:**
  - Tokenization and sequence modeling
  - LSTM-based RNN for next-word generation
  - Interactive web app using Streamlit
- **Skills Used:** TensorFlow, Keras, NLP, Streamlit, HuggingFace Datasets

---

### 📈 3. Exploratory Data Analysis on Global Superstore Sales Dataset

- **Objective:** Derive business insights from retail sales data through EDA.
- **Dataset:** Global Superstore Sales dataset (CSV).
- **Features:**
  - Data cleaning, preprocessing, and handling missing values
  - Univariate, bivariate, and multivariate visual analysis
  - Business recommendations based on trends and patterns
- **Skills Used:** Pandas, Seaborn, Matplotlib, Plotly, Data Cleaning, Visualization

---

## 🛠 Requirements

Each branch contains its own `requirements.txt` file.  
To set up a project:

```bash
git checkout <branch-name>
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt

________________________________________________________________________________________________________________________________________________________________________________________________________
📬 About
This repository was developed as part of the GUVI Final Project Submission for demonstrating end-to-end ML/NLP/EDA workflows and real-world deployment strategies.

📌 Note
Make sure to switch to the appropriate branch (pneumonia-detection, next-word-prediction, or eda-superstore-analysis) to explore the individual project code and documentation.


