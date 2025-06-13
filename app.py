import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('xgb_model_tuned.pkl')

# Judul aplikasi
st.title("Prediksi Harga Rumah (dalam Juta Rupiah)")

st.markdown("Masukkan informasi rumah di bawah ini:")

# Input fitur sesuai dataset
lb = st.number_input("Luas Bangunan (LB) - m²", min_value=0, value=100)
lt = st.number_input("Luas Tanah (LT) - m²", min_value=0, value=100)
kt = st.number_input("Jumlah Kamar Tidur (KT)", min_value=0, value=3)
km = st.number_input("Jumlah Kamar Mandi (KM)", min_value=0, value=2)
grs = st.number_input("Jumlah Garasi (GRS)", min_value=0, value=1)

# Tombol prediksi
if st.button("Prediksi Harga"):
    fitur = np.array([[lb, lt, kt, km, grs]])
    hasil_prediksi = model.predict(fitur)[0]
    st.success(f"Perkiraan Harga Rumah: {hasil_prediksi:.2f} juta rupiah")
