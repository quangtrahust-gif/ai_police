# bai12_4.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5

plt.figure(figsize=(8,5))
plt.scatter(x, y, alpha=0.6, c='green', edgecolors='k')
plt.title('Mối quan hệ giữa X và Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.savefig('scatter.png')
plt.show()
