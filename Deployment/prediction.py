import tensorflow as tf
# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)
import streamlit as st
import pandas as pd
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import pickle
import json


# Load All Files
from tensorflow.keras.models import load_model


model = load_model('model.h5')

def run():
    st.title('Sentiment Analysis')
    # Membuat form
    with st.form(key='form_parameters'):
        
        tweet= st.text_area('Text', value="", height=None, max_chars=None, key=None)

        submitted = st.form_submit_button('Predict')

    if submitted:       
        # Tokenize and pad the sequences for the test data
        max_features = 10000
        max_words = 10
        tokenizer = Tokenizer(num_words=max_features)
        tokenizer.fit_on_texts([tweet])
        X_test = tokenizer.texts_to_sequences([tweet])
        X_test_padded = pad_sequences(X_test, maxlen=max_words)

        # Predict the sentiment of the test data
        y_pred = model.predict(X_test_padded)

        # Define the labels for sentiment classes
        labels = ["Negative", "Neutral", "Positive"]
        
        # Convert the predicted probabilities into sentiment labels
        y_pred_labels = labels[np.argmax(y_pred)]

        st.write("Predicted sentiment: ", y_pred_labels)

if __name__ == '__main__':
    run()
