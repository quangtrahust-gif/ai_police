# bai5_4.py
a = int(input("Nhập cơ số: "))
b = int(input("Nhập số mũ (>=0): "))
ket_qua = 1
i = 0
while i < b:
    ket_qua *= a
    i += 1
print(f"{a}^{b} = {ket_qua}")
