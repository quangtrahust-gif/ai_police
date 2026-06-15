# bai10_4.py
import numpy as np

# Thêm vô hướng
A = np.ones((3,3))
print("A + 2:\n", A + 2)

# Hàng cộng với vector
row = np.array([1,2,3])
print("A + row:\n", A + row)

# Cột cộng với vector
col = np.array([[1],[2],[3]])
print("A + col:\n", A + col)

# Nhân ma trận (dot product)
X = np.array([[1,2],[3,4]])
Y = np.array([[5,6],[7,8]])
dot_product = np.dot(X, Y)  # hoặc X @ Y
print("Matrix multiplication:\n", dot_product)
