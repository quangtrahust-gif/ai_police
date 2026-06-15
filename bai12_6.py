# bai12_6.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x/3) * np.sin(x)
data = np.random.normal(0, 1, 1000)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0,0].plot(x, y1, 'r-')
axes[0,0].set_title('Sin(x)')
axes[0,0].grid(True)

axes[0,1].plot(x, y2, 'b-')
axes[0,1].set_title('Cos(x)')
axes[0,1].grid(True)

axes[1,0].plot(x, y3, 'g-')
axes[1,0].set_title('Damping')
axes[1,0].grid(True)

axes[1,1].hist(data, bins=30, color='purple', alpha=0.7)
axes[1,1].set_title('Histogram')
axes[1,1].grid(axis='y')

plt.tight_layout()
plt.savefig('subplots.png')
plt.show()
