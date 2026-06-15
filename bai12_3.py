# bai12_3.py
import matplotlib.pyplot as plt

labels = ['Samsung', 'Apple', 'Xiaomi', 'Others']
sizes = [45, 30, 15, 10]
colors = ['gold', 'silver', 'lightcoral', 'lightblue']
explode = (0.05, 0, 0, 0)  # tách nhẹ phần Samsung

plt.figure(figsize=(6,6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Thị phần điện thoại')
plt.axis('equal')  # đảm bảo hình tròn
plt.savefig('market_share.png')
plt.show()
