import matplotlib.pyplot as plt

# Dữ liệu
thang = [1, 2, 3, 4, 5, 6]
doanh_so = [120, 135, 150, 170, 190, 210]

plt.figure(figsize=(8,5))
plt.plot(thang, doanh_so, marker='o', linestyle='-', color='b', linewidth=2, markersize=8)
plt.title('Doanh số theo tháng')
plt.xlabel('Tháng')
plt.ylabel('Doanh số (triệu VND)')
plt.grid(True)
plt.savefig('doanh_so.png', dpi=100)
plt.show()
