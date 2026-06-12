# bai8_5.py
# Danh sách sản phẩm (mỗi sản phẩm là dictionary)
san_pham = [
    {"id": 1, "ten": "Bút bi", "gia": 5000},
    {"id": 2, "ten": "Vở", "gia": 15000},
    {"id": 3, "ten": "Thước", "gia": 8000}
]

# Hiển thị
print("Danh sách sản phẩm:")
for sp in san_pham:
    print(f"{sp['id']}. {sp['ten']} - {sp['gia']:,} VND")

# Tìm sản phẩm theo tên (không phân biệt hoa thường)
tim = input("Nhập tên sản phẩm cần tìm: ").lower()
found = None
for sp in san_pham:
    if sp['ten'].lower() == tim:
        found = sp
        break
if found:
    print(f"Tìm thấy: {found['ten']} - Giá {found['gia']:,} VND")
else:
    print("Không tìm thấy sản phẩm.")
