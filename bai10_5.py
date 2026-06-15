# bai10_5.py
import numpy as np

data = np.random.randint(1, 100, size=(4,5))  # 4x5 số ngẫu nhiên 1-99
print("Dữ liệu:\n", data)

print("Tổng:", np.sum(data))
print("TB cột:", np.mean(data, axis=0))
print("TB hàng:", np.mean(data, axis=1))
print("Max toàn bộ:", np.max(data))
print("Min theo cột:", np.min(data, axis=0))
print("Vị trí max toàn bộ:", np.argmax(data))
