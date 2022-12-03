import pickle
import streamlit as st

# membaca model
milk_model =  pickle.load(open('milk_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Kualitas Susu')

pH = st.text_input('Kehalusan PH susu')

Temprature = st.text_input('Masukan suhu susu')

Taste = st.text_input('Masukan Rasa susu')

Odor = st.text_input('Masukan aroma susu')

Fat = st.text_input('Masukan kandungan lemak pada susu')

Turbidity = st.text_input('Masukan Kekeruhan Susu')

Colour = st.text_input('Masukan warna susu')

# code untuk kelompok jenis bunga
milk_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    milk_prediction = milk_model.predict([[pH, Temprature, Taste, Odor, Fat, Turbidity, Colour]])
    if(milk_prediction[0] == 0):
       milk_diagnosis ='low'
    elif(milk_prediction[0]==1):
        milk_diagnosis ='medium'
    else :
        milk_diagnosis ='high'

st.success(milk_diagnosis)
