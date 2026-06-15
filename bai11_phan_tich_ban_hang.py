import pandas as pd
import numpy as np

# 1. Tạo dữ liệu
np.random.seed(1)
dates = pd.date_range('2025-06-01', periods=20, freq='D')
products = np.random.choice(['A','B','C','D'], 20)
sales = np.random.randint(100, 1001, 20)
quantities = np.random.randint(1, 51, 20)

df = pd.DataFrame({'Ngày': dates, 'Sản phẩm': products, 'Doanh số': sales, 'Số lượng': quantities})

# 2. Ghi CSV
df.to_csv('sales.csv', index=False)

# 3. Đọc lại
df2 = pd.read_csv('sales.csv', parse_dates=['Ngày'])

# 4. Tính toán
total_by_product = df2.groupby('Sản phẩm')['Doanh số'].sum()
avg_daily_sales = df2.groupby('Ngày')['Doanh số'].mean()
max_sales_date = df2.loc[df2['Doanh số'].idxmax(), 'Ngày']

# 5. Thêm cột Doanh thu
df2['Doanh thu'] = df2['Doanh số'] * df2['Số lượng']

# 6. Lọc doanh thu > 20000
high_revenue = df2[df2['Doanh thu'] > 20000]

# 7. Xuất Excel với nhiều sheet
with pd.ExcelWriter('sales_summary.xlsx') as writer:
    df2.to_excel(writer, sheet_name='Chi tiết', index=False)
    total_by_product.to_excel(writer, sheet_name='Tổng hợp sản phẩm')
