# bai12_5.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
diem = np.random.normal(loc=6.5, scale=1.2, size=200)
diem = np.clip(diem, 0, 10)  # giới hạn 0-10

plt.figure(figsize=(8,5))
plt.hist(diem, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Phân bố điểm thi của 200 học sinh')
plt.xlabel('Điểm')
plt.ylabel('Tần số')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('histogram.png')
plt.show()
