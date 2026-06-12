# bai8_4.py
chuoi = input("Nhập một chuỗi: ")
dem = {}

for ky_tu in chuoi:
    if ky_tu in dem:
        dem[ky_tu] += 1
    else:
        dem[ky_tu] = 1

print("Số lần xuất hiện của các ký tự:")
for ky_tu, so_lan in dem.items():
    if ky_tu != ' ':
        print(f"'{ky_tu}': {so_lan}")
