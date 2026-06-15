import numpy as np

# Tạo mảng từ list
a = np.array([10, 20, 30, 40])
print("a:", a)
print("Shape:", a.shape, "Dimension:", a.ndim, "Size:", a.size)

# Tạo ma trận 2x3
b = np.array([[1,2,3], [4,5,6]])
print("\nb:\n", b)
print("Shape:", b.shape)

# Tạo mảng đặc biệt
zeros = np.zeros((2,3))
ones = np.ones((2,3))
eye = np.eye(3)
rand = np.random.rand(3,3)
print("\nZeros:\n", zeros)
print("Ones:\n", ones)
print("Eye:\n", eye)
print("Rand:\n", rand)
