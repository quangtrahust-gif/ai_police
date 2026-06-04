# bai4_5.py
numbers = [3, 7, 2, 9, 5, 1]
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print(f"Số lớn nhất: {max_val}")
