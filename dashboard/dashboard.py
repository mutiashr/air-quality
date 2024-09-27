import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = 'PRSA_Data_Shunyi_20130301-20170228.csv'
data = pd.read_csv(file_path)

# Data Cleaning and Preparation
data['datetime'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']])
data.set_index('datetime', inplace=True)
data['PM2.5'].fillna(data['PM2.5'].median(), inplace=True)
data['TEMP'].fillna(data['TEMP'].median(), inplace=True)

# Streamlit Dashboard
st.title("Dashboard Analisis Data Polusi Udara PM2.5 di Shunyi")

# Menampilkan Data
st.subheader("Data Polusi Udara")
st.write(data.head())

# Pertanyaan 1
st.subheader("Pertanyaan 1: Bagaimana tren dan fluktuasi tingkat PM2.5 selama beberapa tahun terakhir?")
annual_pm25 = data['PM2.5'].resample('Y').mean()

# Visualisasi Tren PM2.5
plt.figure(figsize=(10, 6))
plt.plot(annual_pm25.index, annual_pm25.values, marker='o', linestyle='-', color='b')
plt.title('Tren Tahunan PM2.5 (2013-2017)')
plt.xlabel('Tahun')
plt.ylabel('Rata-rata PM2.5')
plt.grid(True)
st.pyplot(plt)

# Menghitung rata-rata bulanan PM2.5
monthly_pm25 = data['PM2.5'].resample('M').mean()

# Visualisasi Tren Bulanan PM2.5
plt.figure(figsize=(9, 6))
plt.plot(monthly_pm25.index, monthly_pm25.values, color='g', linestyle='-', marker='o')
plt.title('Tren Bulanan PM2.5 (2013-2017)', fontsize=16)
plt.xlabel('Waktu', fontsize=12)
plt.ylabel('Rata-rata PM2.5', fontsize=12)
plt.grid(True)
st.pyplot(plt)  # Menggunakan Streamlit untuk menampilkan plot


# Hasil Analisis
st.subheader("Hasil Analisis")
st.write("**Hasil Analisis:**")
st.write("- **Tren Tahunan**: Dari 2013 hingga 2017, tingkat PM2.5 mengalami fluktuasi. Namun, ternyata polusi PM2.5 tidak selalu stabil. Ada saat-saat di mana polusi lebih tinggi dan ada tahun di mana polusi menurun.")
st.write("- **Tren Musiman**: PM2.5 lebih tinggi di musim dingin dan lebih rendah di musim panas, menunjukkan pola musiman yang konsisten.")

# Pertanyaan 2
st.subheader("Pertanyaan 2: Apakah suhu udara yang lebih rendah cenderung berkaitan dengan meningkatnya PM2.5?")
# Visualisasi Hubungan Suhu dan PM2.5
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['TEMP'], y=data['PM2.5'], alpha=0.5)
plt.title('Hubungan antara Suhu Udara dan PM2.5')
plt.xlabel('Suhu Udara (°C)')
plt.ylabel('PM2.5')
plt.grid(True)
st.pyplot(plt)

# Hasil Analisis
st.subheader("Hasil Analisis")
st.write("**Hasil Analisis:**")
st.write("- **Scatter Plot**: Saat suhu turun, PM2.5 cenderung meningkat, menunjukkan hubungan negatif.")
st.write("- **Korelasi**: Nilai korelasi negatif mengindikasikan suhu rendah berkaitan dengan peningkatan PM2.5.")


# Deskripsi Data
st.subheader("Deskripsi Data")
st.write("""
Data yang dianalisis berfokus pada polusi udara di wilayah Shunyi, China, selama periode 2013 hingga 2017. Data ini mencakup berbagai variabel penting terkait kualitas udara dan kondisi cuaca, di antaranya:
- **PM2.5**: Konsentrasi partikel halus di udara (<2.5 mikrometer) yang berbahaya karena dapat terhirup dan masuk ke aliran darah.
- **Temperatur (TEMP)**: Suhu udara yang diukur, penting untuk memahami pengaruh cuaca terhadap polusi udara.
- **Variabel cuaca lainnya**: Kecepatan angin, tekanan udara, dan curah hujan, yang memengaruhi distribusi polutan dan tingkat polusi.
""")

# Kesimpulan
st.subheader("Kesimpulan")
st.write("1. **Perubahan PM2.5 dari Tahun ke Tahun**:")
st.write("- Tingkat PM2.5 tidak stabil, terdapat fluktuasi dari tahun ke tahun.")
st.write("- **Temuan**: Bulan-bulan musim dingin (Desember-Februari) memiliki tingkat PM2.5 yang lebih tinggi dibandingkan bulan-bulan musim panas.")
st.write("- **Data**: Rata-rata tahunan menunjukkan peningkatan di bulan dingin, dengan puncaknya terjadi di bulan Desember.")

st.write("2. **Hubungan Suhu dan PM2.5**:")
st.write("- Saat suhu udara turun, tingkat PM2.5 cenderung meningkat.")
st.write("- **Temuan**: Suhu yang lebih rendah berhubungan dengan peningkatan polusi udara.")
st.write("- **Data**: Korelasi negatif antara suhu dan PM2.5 menunjukkan bahwa semakin rendah suhu, semakin tinggi tingkat polusi, kemungkinan disebabkan oleh angin yang lebih tenang di musim dingin.")
