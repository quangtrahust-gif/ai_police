#bai3_6.py
Ten = input("Nhập tên của bạn: ")
Diem_toan = float(input("Nhập điểm môn Toán: "))
Diem_van =  float(input("'Nhập điểm môn văn: "))
Diem_anh  = float(input("Nhập điểm môn Anh: "))
diem_tb = (Diem_toan*2 + Diem_van + Diem_anh)/4
if diem_tb  >= 8.0:
    xep_loai = "Giỏi"
elif diem_tb  >= 6.5:
    xep_loai = "Khá"
elif diem_tb  >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"
print(f"Học sinh {Ten}, Điểm TB {diem_tb} → Xếp loại: {xep_loai}")
