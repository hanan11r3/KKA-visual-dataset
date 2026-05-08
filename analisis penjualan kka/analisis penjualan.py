import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
df = pd.read_csv('data_praktikum_analisis_data.csv')

# Cek data awal
print(df.head())
print(df.info())
print(df.isnull().sum())

# 2. Perbaikan Baris 10: Gunakan 'df' bukan nama file
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# 3. Ekstrak Bulan untuk Tren Penjualan
df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

# 4. Visualisasi Tren Penjualan
plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b')
plt.title('Tren Penjualan Bulanan')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7) # Opsional: Tambah grid agar lebih rapi
plt.show()

# 5. Analisis Korelasi
# Catatan: Sesuaikan kolom dengan yang ada di CSV (Quantity, Price_Per_Unit, Ad_Budget, Total_Sales)
columns_to_corr = ['Total_Sales', 'Ad_Budget', 'Quantity', 'Price_Per_Unit']
correlation = df[columns_to_corr].corr()

# 6. Visualisasi Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Peta Korelasi Antar Variabel')
plt.show()