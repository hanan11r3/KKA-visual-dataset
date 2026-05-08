import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv ('data_praktikum_analisis_data.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())

df['Order_Date'] = pd. to_datetime(data['Order_Date'])
df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Total_Sales'].sum()
plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b')
plt.title('Tren Penjualan Bulanan')
plt.xticks(rotation=45)
plt.show()

correlation = df[['Total_Sales', 'Ad_Budget', 'Discount_Percentage']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Peta Korelasi Antar Variabel')
plt.show()