# bai11_6.py
import pandas as pd

# Tạo DataFrame mẫu
df = pd.DataFrame({
    'STT': [1,2,3],
    'Họ tên': ['An', 'Bình', 'Chi'],
    'Điểm': [8,7,9]
})

# Ghi ra CSV
df.to_csv('ket_qua.csv', index=False, encoding='utf-8')
print("Đã ghi file CSV")

# Ghi ra Excel (cần cài openpyxl: pip install openpyxl)
df.to_excel('ket_qua.xlsx', index=False)
print("Đã ghi file Excel")
# Đọc lại CSV
df_doc = pd.read_csv('ket_qua.csv')
print("Đọc từ CSV:\n", df_doc)
