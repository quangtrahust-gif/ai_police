# bai8_quan_ly_ho_so_nhan_vien.py

# Bắt đầu với danh sách rỗng
nhan_vien = []

# Tạo mã tự động
def tao_ma_tu_dong(ds):
    return f"NV{len(ds)+1:03d}"

# Nhập thông tin (không cần tham số ma, sẽ tự gọi hàm tạo mã)
def nhap_nhan_vien(ds):
    ma = tao_ma_tu_dong(ds)
    ten = input("Họ tên: ")
    phong = input("Phòng ban: ")
    # Kiểm tra lương hợp lệ
    while True:
        try:
            luong = float(input("Lương: "))
            if luong > 0:
                break
            else:
                print("Lương phải lớn hơn 0!")
        except ValueError:
            print("Vui lòng nhập số!")
    return {"ma_nv": ma, "ho_ten": ten, "phong_ban": phong, "luong": luong}

# Hiển thị bảng
def hien_thi(ds):
    if not ds:
        print("\nDanh sách nhân viên trống.")
        return
    print("\nMã NV | Họ tên             | Phòng ban     | Lương")
    print("-" * 60)
    for nv in ds:
        print(f"{nv['ma_nv']:<5} | {nv['ho_ten']:<18} | {nv['phong_ban']:<12} | {nv['luong']:,.0f} VND")

# Tìm nhân viên theo mã hoặc tên
def tim_nhan_vien(ds):
    if not ds:
        print("Danh sách trống, không thể tìm.")
        return
    keyword = input("Nhập mã NV hoặc họ tên cần tìm: ").lower()
    ket_qua = []
    for nv in ds:
        if keyword in nv['ma_nv'].lower() or keyword in nv['ho_ten'].lower():
            ket_qua.append(nv)
    if ket_qua:
        hien_thi(ket_qua)
    else:
        print("Không tìm thấy nhân viên nào.")

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

# --- Menu chính ---
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
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1-5.")
