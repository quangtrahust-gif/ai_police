# bai7_quan_ly_sinh_vien_nang_cao.py

def tinh_diem_trung_binh(toan, van, anh):
    """Tính điểm trung bình hệ số (Toán nhân 2)"""
    return (2 * toan + van + anh) / 4

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
    while True:
        try:
            diem = float(input(f"Nhập điểm {mon}: "))
            if 0 <= diem <= 10:
                return diem
            print("Điểm phải từ 0 đến 10, mời nhập lại!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

def nhap_sinh_vien():
    """Nhập thông tin một sinh viên và trả về dictionary"""
    ten = input("Tên sinh viên: ")
    toan = nhap_diem_mon("Toán")
    van = nhap_diem_mon("Văn")
    anh = nhap_diem_mon("Anh")
    dtb = tinh_diem_trung_binh(toan, van, anh)
    loai = xep_loai(dtb)
    return {
        "ten": ten,
        "toan": toan,
        "van": van,
        "anh": anh,
        "dtb": dtb,
        "xep_loai": loai
    }

def hien_thi_danh_sach(danh_sach):
    """Hiển thị danh sách sinh viên dạng bảng"""
    if not danh_sach:
        print("\nDanh sách sinh viên trống.")
        return
    print("\nSTT | Họ tên             | ĐTB  | Xếp loại")
    print("-" * 50)
    for i, sv in enumerate(danh_sach, start=1):
        # Căn chỉnh tên tối đa 18 ký tự
        ten = sv['ten'][:18] if len(sv['ten']) > 18 else sv['ten']
        print(f"{i:<3} | {ten:<18} | {sv['dtb']:<5.2f} | {sv['xep_loai']}")

# --- Chương trình chính ---
danh_sach_sinh_vien = []

while True:
    print("\n=== QUẢN LÝ SINH VIÊN NÂNG CAO ===")
    print("1. Thêm sinh viên")
    print("2. Hiển thị danh sách")
    print("3. Thoát")
    chon = input("Chọn: ")

    if chon == "1":
        sv = nhap_sinh_vien()
        danh_sach_sinh_vien.append(sv)
        print(f"Đã thêm sinh viên {sv['ten']}, ĐTB = {sv['dtb']:.2f}, Xếp loại: {sv['xep_loai']}")

    elif chon == "2":
        hien_thi_danh_sach(danh_sach_sinh_vien)

    elif chon == "3":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1, 2 hoặc 3.")
