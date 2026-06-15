import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Tạo dữ liệu nếu chưa có file sales.csv
# ... (tương tự ngày 11)
# 1. Tạo dữ liệu
np.random.seed(1)
dates = pd.date_range('2025-06-01', periods=20, freq='D')
products = np.random.choice(['A','B','C','D'], 20)
sales = np.random.randint(100, 1001, 20)
quantities = np.random.randint(1, 51, 20)

df = pd.DataFrame({'Ngày': dates, 'Sản phẩm': products, 'Doanh số': sales, 'Số lượng': quantities})
df.to_csv('sales.csv', index=False)
# 2. Đọc dữ liệu
df = pd.read_csv('sales.csv', parse_dates=['Ngày'])

# 3. Tính toán
total_by_product = df.groupby('Sản phẩm')['Doanh số'].sum()
avg_daily_sales = df.groupby('Ngày')['Doanh số'].mean()
max_date = df.loc[df['Doanh số'].idxmax(), 'Ngày']

print("Tổng doanh số theo sản phẩm:\n", total_by_product)
print("Ngày có doanh số cao nhất:", max_date)

# 4. Vẽ biểu đồ cột
plt.figure()
total_by_product.plot(kind='bar', color=['blue','green','red'])
plt.title('Tổng doanh số theo sản phẩm')
plt.ylabel('Doanh số')
plt.savefig('total_by_product.png')
plt.show()

# 5. Biểu đồ đường doanh số theo ngày
plt.figure()
df.groupby('Ngày')['Doanh số'].sum().plot(marker='o')
plt.title('Doanh số theo ngày')
plt.xlabel('Ngày')
plt.ylabel('Doanh số')
plt.grid(True)
plt.savefig('daily_sales.png')
plt.show()

# 6. Biểu đồ tròn
plt.figure()
total_by_product.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Tỷ lệ đóng góp doanh số')
plt.ylabel('')
plt.savefig('pie_chart.png')
plt.show()

# 7. Histogram
plt.figure()
df['Doanh số'].hist(bins=15, edgecolor='black')
plt.title('Phân bố doanh số')
plt.xlabel('Doanh số')
plt.ylabel('Tần số')
plt.savefig('hist_sales.png')
plt.show()
