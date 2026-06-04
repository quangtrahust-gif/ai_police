n = int(input("Nhập một số nguyên không âm: "))

# Kiểm tra đầu vào hợp lệ
if n < 0:
    print("Vui lòng nhập số không âm!")
else:
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    print(f"Giai thừa của {n} là {ket_qua}")
