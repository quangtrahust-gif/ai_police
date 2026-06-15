# bai11_3.py
import pandas as pd

df = pd.DataFrame({
    'Sản phẩm': ['A', 'B', 'C'],
    'Giá': [100, 200, 150],
    'Số lượng': [5, 3, 10]
})

# Thêm cột Thành tiền
df['Thành tiền'] = df['Giá'] * df['Số lượng']
print("Sau thêm cột:\n", df)

# Sửa cột Giá (tăng 10%)
df['Giá'] = df['Giá'] * 1.1
print("Sau tăng giá 10%:\n", df)

# Xóa cột Số lượng
df.drop('Số lượng', axis=1, inplace=True)
print("Sau xóa cột Số lượng:\n", df)
