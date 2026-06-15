# bai12_7.py
import pandas as pd
import matplotlib.pyplot as plt

# Tạo DataFrame
df = pd.DataFrame({
    'Tháng': ['T1','T2','T3','T4','T5','T6'],
    'Doanh số': [120, 135, 150, 170, 190, 210],
    'Chi phí': [80, 85, 90, 95, 100, 110]
})

# Vẽ đường
plt.figure(figsize=(8,5))
plt.plot(df['Tháng'], df['Doanh số'], marker='o', label='Doanh số')
plt.plot(df['Tháng'], df['Chi phí'], marker='s', label='Chi phí')
plt.xlabel('Tháng')
plt.ylabel('Triệu VND')
plt.title('Doanh số và chi phí 6 tháng')
plt.legend()
plt.grid(True)
plt.show()

# Vẽ cột nhóm (dùng pandas plot)
df.plot(x='Tháng', kind='bar', stacked=False, figsize=(8,5))
plt.title('So sánh doanh số và chi phí')
plt.ylabel('Triệu VND')
plt.show()