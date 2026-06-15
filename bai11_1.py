import pandas as pd
import numpy as np

# Tạo dữ liệu mẫu
data = {
    'Sinh viên': ['An', 'Bình', 'Chi', 'Dũng', 'Giang'],
    'Toán': [8, 7, 9, 6, 8],
    'Lý': [7, 8, 8, 5, 9],
    'Hóa': [9, 6, 7, 7, 8]
}
df = pd.DataFrame(data)

print("=== DỮ LIỆU BAN ĐẦU ===")
print(df)

print("\n=== 5 DÒNG ĐẦU ===")
print(df.head())

print("\n=== THÔNG TIN DataFrame ===")
print(df.info())

print("\n=== THỐNG KÊ MÔ TẢ ===")
print(df.describe())
