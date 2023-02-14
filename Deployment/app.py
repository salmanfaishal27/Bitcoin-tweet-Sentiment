import streamlit as st
import Home
import prediction

navigation = st.sidebar.selectbox('Pilihan Halaman :', ('Home', 'Sentimen Analyze'))

if navigation == 'Home':
    Home.run()
else:
    prediction.run()