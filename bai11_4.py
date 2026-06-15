# bai11_4.py
import pandas as pd

# Đọc file CSV
df = pd.read_csv('data.csv')
print("Dữ liệu gốc:\n", df)

# Kiểm tra null
print("Số null mỗi cột:\n", df.isnull().sum())

# Xóa hàng có null
df_drop = df.dropna()
print("Sau khi xóa null:\n", df_drop)

# Điền giá trị (fillna)
df_fill = df.copy()
df_fill['Tuổi'] = df_fill['Tuổi'].fillna(df_fill['Tuổi'].mean())  # điền TB
df_fill['Điểm'] = df_fill['Điểm'].fillna(0)
print("Sau khi điền giá trị:\n", df_fill)
