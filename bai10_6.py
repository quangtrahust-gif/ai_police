# bai10_6.py
import numpy as np

arr = np.array([1,5,2,8,3,9,4])

# Lấy các phần tử > 5
filtered = arr[arr > 5]
print("arr > 5:", filtered)

# Điều kiện kết hợp
filtered2 = arr[(arr > 3) & (arr < 8)]
print("3 < arr < 8:", filtered2)

# Thay đổi các phần tử thỏa mãn
arr[arr > 5] = 100
print("Sau khi gán 100 cho >5:", arr)
