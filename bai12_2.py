# bai12_2.py
import matplotlib.pyplot as plt

san_pham = ['A', 'B', 'C', 'D']
luong_ban = [250, 180, 300, 210]

plt.figure(figsize=(6,4))
plt.bar(san_pham, luong_ban, color=['red', 'green', 'blue', 'orange'])
plt.title('Số lượng bán theo sản phẩm')
plt.xlabel('Sản phẩm')
plt.ylabel('Số lượng')
for i, v in enumerate(luong_ban):
    plt.text(i, v + 5, str(v), ha='center')
plt.savefig('san_pham_bar.png')
plt.show()
