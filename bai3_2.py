# bai3_2.py
diem = float(input("Nhập điểm trung bình (0-10): "))
if diem >= 8.5:
    xep_loai = "Giỏi"
elif diem >= 7.0:
    xep_loai = "Khá"
elif diem >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"
print(f"Điểm {diem} → Xếp loại: {xep_loai}")
