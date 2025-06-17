import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from utils.preprocessing import load_and_prepare_data, save_tokenizer

print("Loading and preparing data...")
X, y, tokenizer, vocab_size = load_and_prepare_data(seq_length=5, num_words=20000)

print("Building model...")
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=64, input_length=X.shape[1]))
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(128))
model.add(Dense(128, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))

# Use sparse_categorical_crossentropy to avoid one-hot encoding
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print("Training model...")
model.fit(X, y, epochs=10, batch_size=256)

print("Saving model and tokenizer...")
model.save("model/next_word_model.h5")
save_tokenizer(tokenizer)
