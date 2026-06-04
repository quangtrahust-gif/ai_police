# bai4_2.py
n = int(input("Nhập N: "))
tong = 0
for i in range(1, n+1):
    tong += i   # tương đương tong = tong + i
print(f"Tổng từ 1 đến {n} là {tong}")
