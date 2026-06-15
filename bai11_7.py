# bai11_7.py
import numpy as np
import pandas as pd

# Tạo dữ liệu điểm của 10 sinh viên
np.random.seed(42)
sv = [f'SV{i:02d}' for i in range(1,11)]
toan = np.random.randint(4,10,10)
van = np.random.randint(5,9,10)
anh = np.random.randint(4,10,10)

df = pd.DataFrame({'MSSV': sv, 'Toán': toan, 'Văn': van, 'Anh': anh})
df['ĐTB'] = (df['Toán']*2 + df['Văn'] + df['Anh']) / 4

print("=== Bảng điểm ===")
print(df)

# Thống kê
print("\n=== Thống kê mô tả ===")
print(df[['Toán','Văn','Anh','ĐTB']].describe())

# Xếp loại
def xep_loai(dtb):
    if dtb >= 8.5:
        return 'Giỏi'
    elif dtb >= 6.5:
        return 'Khá'
    elif dtb >= 5:
        return 'TB'
    else:
        return 'Yếu'

df['Xếp loại'] = df['ĐTB'].apply(xep_loai)
print("\n=== Bảng xếp loại ===")
print(df[['MSSV', 'ĐTB', 'Xếp loại']])

# Số lượng mỗi loại
print("\nSố lượng xếp loại:\n", df['Xếp loại'].value_counts())
