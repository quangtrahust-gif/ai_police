# bai11_2.py
import pandas as pd

data = {
    'Tên': ['An', 'Bình', 'Chi', 'Dũng', 'Giang'],
    'Tuổi': [20, 22, 21, 23, 20],
    'Điểm_TB': [8.2, 7.5, 8.9, 6.8, 8.5]
}
df = pd.DataFrame(data)

# Chọn cột
print("Cột Tên:\n", df['Tên'])
print("Cột Tên và Điểm_TB:\n", df[['Tên', 'Điểm_TB']])

# Lọc sinh viên có Điểm_TB >= 8
print("Sinh viên giỏi (ĐTB>=8):\n", df[df['Điểm_TB'] >= 8])

# Lọc sinh viên tuổi 20 và ĐTB>=8
print("Tuổi 20 và ĐTB>=8:\n", df[(df['Tuổi'] == 20) & (df['Điểm_TB'] >= 8)])
