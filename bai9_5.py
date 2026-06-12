# bai9_5.py
def nhap_so_nguyen(prompt):
    while True:
        try:
            n = int(input(prompt))
            return n
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên!")

n = nhap_so_nguyen("Nhập số lượng sinh viên: ")
with open("sinhvien.txt", "w", encoding="utf-8") as f:
    for i in range(n):
        ten = input(f"Sinh viên thứ {i+1}: ")
        f.write(ten + "\n")
print("Đã lưu")
