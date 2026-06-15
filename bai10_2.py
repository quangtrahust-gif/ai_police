# bai10_2.py
import numpy as np

arr = np.array([[10,20,30,40],
                [50,60,70,80],
                [90,100,110,120]])

print("Hàng thứ 1:", arr[1])
print("Cột thứ 2:", arr[:, 2])
print("Ô (1,2):", arr[1,2])
print("Hàng 0-1, cột 1-3:\n", arr[0:2, 1:4])
