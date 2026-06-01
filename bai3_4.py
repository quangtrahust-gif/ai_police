# bai3_4.py
so_km = float(input("Số km đã đi: "))
if so_km <= 0:
    tien = 0
elif so_km <= 1:
    tien = so_km * 10000
elif so_km <= 10:
    tien = 10000 + (so_km - 1) * 8000
else:
    tien = 10000 + 9 * 8000 + (so_km - 10) * 5000
print(f"Số km: {so_km}, Tiền taxi: {tien:,.0f} VNĐ")
