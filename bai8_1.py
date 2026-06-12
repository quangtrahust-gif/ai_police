# Tuple: lưu tọa độ và unpacking
diem_a = (3, 5)
diem_b = (7, 9)

# Unpack tuple
x1, y1 = diem_a
x2, y2 = diem_b

# Tính khoảng cách Manhattan
khoang_cach = abs(x1 - x2) + abs(y1 - y2)
print(f"Điểm A: {diem_a}, Điểm B: {diem_b}")
print(f"Khoảng cách Manhattan: {khoang_cach}")

# Hàm trả về nhiều giá trị
def chia_du(a, b):
    return a // b, a % b

thuong, du = chia_du(17, 5)
print(f"17 // 5 = {thuong}, dư {du}")
