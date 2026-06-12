# bai9_7.py
import json

# Danh sách nhân viên (từ bài tập ngày 8)
nhan_vien = [
    {"ma_nv": "NV001", "ho_ten": "Lê Văn An", "phong_ban": "Kỹ thuật", "luong": 15000000},
    {"ma_nv": "NV002", "ho_ten": "Trần Thị Bình", "phong_ban": "Kinh doanh", "luong": 12000000}
]

# Ghi xuống file JSON
with open("nhan_vien.json", "w", encoding="utf-8") as f:
    json.dump(nhan_vien, f, ensure_ascii=False, indent=4)

# Đọc lại từ file JSON
with open("nhan_vien.json", "r", encoding="utf-8") as f:
    du_lieu_doc = json.load(f)
    print("Dữ liệu đọc từ file:")
    for nv in du_lieu_doc:
        print(nv)
