import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    # Membuat title
    st.title('Sentiment Analysis')

    # Membuat Sub Header
    st.subheader('Hacktiv8 Phase 2: Milestone 2')

    # Menambahkan Deskripsi
    st.write('App ini dibuat untuk memprediksi apakah apa sentimen seseorang terhadap tweet bitcoin')
    # Membuat Garis Lurus
    st.markdown('---')
    st.write('Dataset yang digunakan adalah Bitcoin Dataset')

    st.write('Created by: [Salman Faishal](https://github.com/salmanfaishal27)')

if __name__ == '__main__':
    run()