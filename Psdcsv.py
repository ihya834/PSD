import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1.Buat file csv , karena ga rapi saya pakai xlsx
# 2.Load data 
dt = pd.read_excel('DataMahasiswa.xlsx')

print(dt)

# 3.Ambil data kategori
kategori_data = dt[['Jenis Kelamin', 'Jurusan', 'Status']]

print(kategori_data)


# 4.encode
le = LabelEncoder()


dt['Jenis Kelamin'] = le.fit_transform(dt['Jenis Kelamin'])
dt['Jurusan'] = le.fit_transform(dt['Jurusan'])
dt['Status'] = le.fit_transform(dt['Status'])


print(dt)

