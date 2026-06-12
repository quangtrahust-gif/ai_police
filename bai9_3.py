# bai9_3.py
sinh_vien_moi = input("Nhập tên sinh viên mới: ")
with open("ds_sinh_vien.txt", "a", encoding="utf-8") as f:
    f.write(sinh_vien_moi + "\n")
print("Đã thêm")
