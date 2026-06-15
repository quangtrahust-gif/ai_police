import numpy as np

# 1. Tạo mảng 10x5 ngẫu nhiên từ 0-100
np.random.seed(42)  # để kết quả tái hiện
data = np.random.randint(0, 101, size=(10, 5))

# 2. In thông tin
print("Shape:", data.shape)
print("Số chiều:", data.ndim)
print("Tổng số phần tử:", data.size)

# In hàng thứ 3, cột thứ 2
print("Hàng thứ 3:", data[2])
print("Cột thứ 2:", data[:, 1])

# 3. Thống kê
print("Trung bình toàn bộ:", np.mean(data))
print("Max theo cột:", np.max(data, axis=0))
print("Min theo cột:", np.min(data, axis=0))

# 4. Thay thế giá trị
# Gợi ý: dùng boolean indexing
data_copy = data.copy()
data_copy[(data_copy < 20)] = 0
data_copy[(data_copy >= 80)] = 100
print("Sau thay thế:\n", data_copy)

# 5. Lọc các hàng có tổng > 250
row_sums = np.sum(data, axis=1)
filtered_rows = data[row_sums > 250]
print("Các hàng có tổng > 250:\n", filtered_rows)

# 6. Chuẩn hóa cột 0
col0 = data[:, 0]
min_val = np.min(col0)
max_val = np.max(col0)
normalized = (col0 - min_val) / (max_val - min_val)
print("Cột 0 sau chuẩn hóa:\n", normalized)
