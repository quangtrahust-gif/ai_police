# bai6_4.py
def ucln(a, b):
    a_abs = abs(a)
    b_abs = abs(b)
    while b_abs != 0:
        r = a_abs % b_abs
        a_abs = b_abs
        b_abs = r
    return a_abs

# Nhập hai số
x = int(input("Nhập a: "))
y = int(input("Nhập b: "))
print(f"UCLN({x}, {y}) = {ucln(x, y)}")
