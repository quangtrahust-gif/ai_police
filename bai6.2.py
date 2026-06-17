# bai6_2.py
def tinh_giai_thua(n):
    if n < 0:
        return None   # không hợp lệ
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua

# Sử dụng hàm
so = int(input("Nhập số: "))
gt = tinh_giai_thua(so)
if gt is None:
    print("Không tính giai thừa cho số âm")
else:
    print(f"{so}! = {gt}")
