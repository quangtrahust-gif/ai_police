# bai11_5.py
import pandas as pd

# Dữ liệu bán hàng
data = {
    'Phòng ban': ['KD', 'KT', 'KD', 'KT', 'HC', 'KD'],
    'Nhân viên': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Doanh số': [100, 200, 150, 250, 80, 120]
}
df = pd.DataFrame(data)

# Tổng doanh số theo phòng ban
print("Tổng doanh số theo phòng:\n", df.groupby('Phòng ban')['Doanh số'].sum())

# Trung bình doanh số theo phòng
print("TB doanh số theo phòng:\n", df.groupby('Phòng ban')['Doanh số'].mean())

# Nhiều chỉ số
print("Thống kê:\n", df.groupby('Phòng ban')['Doanh số'].agg(['sum', 'mean', 'count']))
