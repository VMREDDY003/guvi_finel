import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from datasets import load_dataset
import pickle

def load_and_prepare_data(seq_length=5, num_words=20000):
    dataset = load_dataset("wikitext", "wikitext-2-raw-v1")
    text = " ".join(dataset['train']['text'])
    text = text.lower().replace('\n', ' ')

    tokenizer = Tokenizer(num_words=num_words, oov_token="<OOV>")
    tokenizer.fit_on_texts([text])
    total_words = min(num_words, len(tokenizer.word_index) + 1)

    input_sequences = []
    token_list = tokenizer.texts_to_sequences([text])[0]

    for i in range(seq_length, len(token_list)):
        n_gram_sequence = token_list[i - seq_length:i + 1]
        input_sequences.append(n_gram_sequence)

    input_sequences = np.array(input_sequences)
    X, y = input_sequences[:, :-1], input_sequences[:, -1]

    return X, y, tokenizer, total_words

def save_tokenizer(tokenizer, path='utils/tokenizer.pkl'):
    with open(path, 'wb') as f:
        pickle.dump(tokenizer, f)

def load_tokenizer(path='utils/tokenizer.pkl'):
    with open(path, 'rb') as f:
        tokenizer = pickle.load(f)
    return tokenizer
