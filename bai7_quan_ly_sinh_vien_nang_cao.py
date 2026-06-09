#bai7_quan_ly_sinh_vien_nang_cao
def Nhap_thong_tin(ten):
    ten = input("Tên của bạn: ")
    return ten
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
print("1.Thêm sinh viên")
print('2.Hiển thị danh sách')
print("3.Thoat")
print("Chọn:1")
# Nhập tên (chuỗi)
ten = input("Tên của bạn: ")

# Nhập điểm
toan = nhap_diem_mon("Toán")
van = nhap_diem_mon("Văn")
anh = nhap_diem_mon("Anh")

# Tính toán và xếp loại
dtb = tinh_diem_trung_binh(toan, van, anh)
hoc_luc = xep_loai(dtb)

# In kết quả (dùng f-string)
print(f"Đã thêm sinh viên {ten}, ĐTB = {dtb:.2f}, Xếp loại: {hoc_luc}")

print("1.Thêm")
print("2.Hiển thị")
print("3.Thoát")

print('Chọn:2')

print( "  STT  " + "|" "  Họ tên  " + "|" + "  ĐTB  " + "|" + " Xếp loại ")
### === QUẢN LÝ SINH VIÊN NÂNG CAO ===
#(1. Thêm sinh viên
#2. Hiển thị danh sách
#3. Thoát
#Chọn: 1
#Nhập tên: Lê Thị B
#Điểm Toán: 9
#Điểm Văn: 8
#Điểm Anh: 8.5
#Đã thêm sinh viên Lê Thị B (ĐTB: 8.62 - Giỏi)

#1. Thêm
#2. Hiển thị
#3. Thoát
#Chọn: 2
#STT | Họ tên          | ĐTB  | Xếp loại
#1   | Nguyễn Văn A    | 8.25 | Khá
#2   | Lê Thị B        | 8.62 | Giỏi ###