import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.ticker as mtick
import seaborn as sns

# โหลดข้อมูล
df = pd.read_csv("Superstore.csv", encoding='ISO-8859-1')

# แปลงคอลัมน์วันที่ให้เป็น datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# สร้างคอลัมน์ Month, Year, Month_Year
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year
df['Month_Year'] = df['Order Date'].dt.to_period('M')

# กรองเฉพาะข้อมูลปี 2017
df_2017 = df[df['Year'] == 2017]

# รวมยอดขายตามเดือนของปี 2017
monthly_sales_2017 = df_2017.groupby('Month_Year')['Sales'].sum().reset_index()
monthly_sales_2017['Month_Year'] = monthly_sales_2017['Month_Year'].astype(str)

# สร้างกราฟ
plt.figure(figsize=(14,6))
ax = sns.lineplot(data=monthly_sales_2017, x='Month_Year', y='Sales', marker='o')

# ปรับ x-axis และ y-axis
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{x:,.0f}'))

# ปรับแต่งกราฟ
plt.xticks(rotation=45)
plt.axhline(monthly_sales_2017['Sales'].mean(), color='red', linestyle='--', label='Average')
plt.legend()
plt.title('Monthly Sales 2017')
plt.xlabel('Month-Year')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()
