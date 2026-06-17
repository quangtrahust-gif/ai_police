# bai6_5.py
def tinh_tong_hieu(a, b):
    tong = a + b
    hieu = a - b
    return tong, hieu

kq = tinh_tong_hieu(10, 3)
print(kq)           # (13, 7)
t, h = tinh_tong_hieu(10, 3)
print(f"Tổng: {t}, Hiệu: {h}")
