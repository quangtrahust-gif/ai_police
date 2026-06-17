# bai7_3.py
diem = [8, 7, 9, 6, 10]
tong = 0
for d in diem:
    tong += d
trung_binh = tong / len(diem)
print(f"Điểm: {diem}")
print(f"Tổng: {tong}, TB: {trung_binh:.2f}")
