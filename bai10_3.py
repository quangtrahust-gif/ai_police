# bai10_3.py
import numpy as np
import time

# So sánh tốc độ NumPy vs list
size = 10**6
list_a = list(range(size))
list_b = list(range(size))

start = time.time()
list_c = [a + b for a, b in zip(list_a, list_b)]
print(f"List time: {time.time()-start:.4f}s")

np_a = np.arange(size)
np_b = np.arange(size)

start = time.time()
np_c = np_a + np_b
print(f"NumPy time: {time.time()-start:.4f}s")
# NumPy thường nhanh hơn 10-100 lần
