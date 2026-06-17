# bai7_4.py
import random
# Tạo list 10 số ngẫu nhiên từ 1-100
so = [random.randint(1, 100) for _ in range(10)]
print("List số:", so)

lon_nhat = so[0]
nho_nhat = so[0]
for x in so:
    if x > lon_nhat:
        lon_nhat = x
    if x < nho_nhat:
        nho_nhat = x
print(f"Lớn nhất: {lon_nhat}, Nhỏ nhất: {nho_nhat}")
