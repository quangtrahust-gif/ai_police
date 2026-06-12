# Bắt đầu với danh sách rỗng
nhan_vien = []

# Tạo mã tự động
def tao_ma_tu_dong(ds):
    return f"NV{len(ds)+1:03d}"

# Nhập thông tin
def nhap_nhan_vien(ma):
    ten = input("Họ tên: ")
    phong = input("Phòng ban: ")
    luong = float(input("Lương: "))
    return {"ma_nv": ma, "ho_ten": ten, "phong_ban": phong, "luong": luong}

# Hiển thị bảng
def hien_thi(ds):
    print("\nMã NV | Họ tên             | Phòng ban     | Lương")
    print("-" * 60)
    for nv in ds:
        print(f"{nv['ma_nv']:<5} | {nv['ho_ten']:<18} | {nv['phong_ban']:<12} | {nv['luong']:,.0f} VND")

# Tổng lương theo phòng ban
def tong_luong_theo_phong(ds):
    phong_ban_set = set(nv['phong_ban'] for nv in ds)
    for phong in phong_ban_set:
        tong = sum(nv['luong'] for nv in ds if nv['phong_ban'] == phong)
        print(f"Phòng {phong}: {tong:,.0f} VND")

# ... phần menu chính
danh_sach_nhan_vien = []

while True:
    print("\n=== QUẢN LÝ NHÂN VIÊN ===")
    print("1. Thêm nhân viên")
    print("2. Hiển thị danh sách")
    print("3. Tìm nhân viên")
    print("4. Tổng lương theo phòng") 
    print("5. Thoát")
    chon = input("Chọn: ")

    if chon == "1":
        nv = nhap_nhan_vien()
        danh_sach_nhan_vien.append(nv)
        print(f"{nv['ma_nv']:<5} | {nv['ho_ten']:<18} | {nv['phong_ban']:<12} | {nv['luong']:,.0f} VND")

    elif chon == "2":
        hien_thi(danh_sach_nhan_vien)

    elif chon == "3":
        hien_thi(danh_sach_nhan_vien)

    elif chon == "4":
        tong_luong_theo_phong(danh_sach_nhan_vien)
        
    elif chon == "5":
        print("Thoát chương trình.")
        break

