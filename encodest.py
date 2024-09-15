import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

st.subheader("Ihya' Ulumuddin")
st.subheader("220411100038")



# 1. Load data dari file Excel
dt = pd.read_excel('DataMahasiswa.xlsx')

# 2. Ambil data kategori
kategori_data = dt[['Jenis Kelamin', 'Jurusan', 'Status']]

# 3. Encode data kategori
le = LabelEncoder()

dt['Jenis Kelamin'] = le.fit_transform(dt['Jenis Kelamin'])
dt['Jurusan'] = le.fit_transform(dt['Jurusan'])
dt['Status'] = le.fit_transform(dt['Status'])

# 4. Tampilkan di Streamlit
# Menampilkan data asli
st.write("Data Asli:")
st.write(dt)

# Menampilkan data kategori
st.write("Data Kategori:")
st.write(kategori_data)

# Menampilkan data yang sudah di-encode
st.write("Data Setelah di Encode:")
st.write(dt)
