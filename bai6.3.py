# bai6_3.py
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Thử nghiệm
for i in range(1, 21):
    if la_nguyen_to(i):
        print(i, end=" ")
print()
