# bai6_quan_ly_sinh_vien.py

def tinh_diem_trung_binh(toan, van, anh):
    """Tính điểm trung bình hệ số (Toán nhân 2)"""
    dtb = (2 * toan + van + anh) / 4
    return dtb

def xep_loai(dtb):
    """Xếp loại học lực dựa trên điểm trung bình"""
    if dtb >= 8.5:
        return "Giỏi"
    elif dtb >= 6.5:
        return "Khá"
    elif dtb >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def nhap_diem_mon(mon):
    """Nhập điểm cho một môn, kiểm tra trong khoảng 0-10"""
    diem = -1
    while diem < 0 or diem > 10:
        try:
            diem = float(input(f"Nhập điểm {mon}: "))
            if diem < 0 or diem > 10:
                print("Điểm phải từ 0 đến 10, mời nhập lại!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
    return diem

# --- Chương trình chính ---
print("=== QUẢN LÝ SINH VIÊN ===")

# Nhập tên (chuỗi)
ten = input("Tên bạn là gì: ")

# Nhập điểm
toan = nhap_diem_mon("Toán")
van = nhap_diem_mon("Văn")
anh = nhap_diem_mon("Anh")

# Tính toán và xếp loại
dtb = tinh_diem_trung_binh(toan, van, anh)
hoc_luc = xep_loai(dtb)

# In kết quả (dùng f-string)
print(f"Sinh viên {ten}, ĐTB = {dtb:.2f}, Xếp loại: {hoc_luc}")
