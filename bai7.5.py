# bai7_5.py
chuoi = ["a", "b", "a", "c", "a", "d", "b"]
ky_tu = input("Nhập ký tự cần đếm: ")
dem = 0
for c in chuoi:
    if c == ky_tu:
        dem += 1
print(f"Ký tự '{ky_tu}' xuất hiện {dem} lần")
