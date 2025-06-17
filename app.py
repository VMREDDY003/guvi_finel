import streamlit as st
from tensorflow.keras.models import load_model
from utils.text_generator import generate_text
from utils.preprocessing import load_tokenizer

# Load model and tokenizer
model = load_model('model/next_word_model.h5')
tokenizer = load_tokenizer()

st.title("🔮 Next Word Prediction using LSTM")
st.write("Type a sequence of words, and the model will try to predict the next word.")

input_text = st.text_input("Enter your text here:", "Deep learning is")

if st.button("Predict Next Word"):
    next_word = generate_text(model, tokenizer, input_text, max_len=5, num_words=1)
    st.success(f"Predicted Next Word: **{next_word}**")
