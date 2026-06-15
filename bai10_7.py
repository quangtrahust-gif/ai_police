# bai10_7.py
import numpy as np

# Reshape
arr = np.arange(12)
reshaped = arr.reshape(3,4)
print("Reshape 3x4:\n", reshaped)

# Flatten (về 1D)
flat = reshaped.flatten()
print("Flatten:", flat)

# Concatenate (nối)
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
c = np.concatenate((a, b), axis=0)  # nối hàng
print("Concatenate:\n", c)

# Split (tách)
split_arr = np.split(reshaped, 3, axis=0)  # tách thành 3 mảng theo hàng
print("Split:", split_arr)
