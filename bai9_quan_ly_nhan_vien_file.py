import json
import os

from bai8_quan_ly_ho_so_nhan_vien import nhap_nhan_vien

FILE_NAME = "nhan_vien.json"

def doc_tu_file():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []   # Không có file, trả về danh sách rỗng
    except json.JSONDecodeError:
        print("Lỗi: File bị hỏng, bắt đầu với danh sách rỗng")
        return []

def ghi_vao_file(ds):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=4)

def tao_ma_tu_dong(ds):
    if not ds:
        return "NV001"
    ma_cuoi = max(int(nv["ma_nv"][2:]) for nv in ds)
    return f"NV{ma_cuoi+1:03d}"

def them_nhan_vien(ds):
    ma = tao_ma_tu_dong(ds)
    ten = input("Họ tên: ")
    phong = input("Phòng ban: ")
    try:
        luong = float(input("Lương: "))
    except ValueError:
        print("Lương không hợp lệ, nhập lại")
        return
    nv = {"ma_nv": ma, "ho_ten": ten, "phong_ban": phong, "luong": luong}
    ds.append(nv)
    ghi_vao_file(ds)
    print(f"Đã thêm nhân viên {ma}")

def xoa_nhan_vien(ds):
    ma = input("Nhập mã nhân viên cần xóa: ")
    for i, nv in enumerate(ds):
        if nv["ma_nv"] == ma:
            ds.pop(i)
            ghi_vao_file(ds)
            print(f"Đã xóa nhân viên {ma}")
            return
    print("Không tìm thấy mã")

def tim_nhan_vien(ds):
    tu_khoa = input("Nhập mã hoặc tên để tìm: ").lower()
    ket_qua = [nv for nv in ds if tu_khoa in nv["ma_nv"].lower() or tu_khoa in nv["ho_ten"].lower()]
    if ket_qua:
        hien_thi(ket_qua)
    else:
        print("Không tìm thấy")
# Hiển thị bảng
def hien_thi(ds):
    if not ds:
        print("\nDanh sách nhân viên trống.")
        return
    print("\nMã NV | Họ tên             | Phòng ban     | Lương")
    print("-" * 60)
    for nv in ds:
        print(f"{nv['ma_nv']:<5} | {nv['ho_ten']:<18} | {nv['phong_ban']:<12} | {nv['luong']:,.0f} VND")
# Tổng lương theo phòng ban
def tong_luong_theo_phong(ds):
    if not ds:
        print("Danh sách trống.")
        return
    phong_ban_set = set(nv['phong_ban'] for nv in ds)
    print("\nTổng lương theo phòng ban:")
    for phong in phong_ban_set:
        tong = sum(nv['luong'] for nv in ds if nv['phong_ban'] == phong)
        so_nv = sum(1 for nv in ds if nv['phong_ban'] == phong)
        print(f"Phòng {phong}: {tong:,.0f} VND (Số NV: {so_nv})")
# ... menu chính
danh_sach_nhan_vien = []

while True:
    print("\n=== QUẢN LÝ NHÂN VIÊN (có lưu file) ===")
    print("1. Thêm nhân viên")
    print("2. Hiển thị danh sách")
    print("3. Tìm nhân viên")
    print("4. Tổng lương theo phòng")
    
    print("6. Thoát")
    chon = input("Chọn: ")

    if chon == "1":
        nv = nhap_nhan_vien(danh_sach_nhan_vien)
        danh_sach_nhan_vien.append(nv)
        print(f"Đã thêm nhân viên: {nv['ma_nv']} - {nv['ho_ten']}")

    elif chon == "2":
        hien_thi(danh_sach_nhan_vien)

    elif chon == "3":
        tim_nhan_vien(danh_sach_nhan_vien)

    elif chon == "4":
        tong_luong_theo_phong(danh_sach_nhan_vien)
    elif chon == "5":
        xoa_nhan_vien(danh_sach_nhan_vien)
    elif chon == "6":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1-6.")

      