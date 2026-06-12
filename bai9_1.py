# Ghi danh sách sinh viên vào file
sinh_vien = ["An", "Bình", "Chi", "Dũng"]

with open("ds_sinh_vien.txt", "w", encoding="utf-8") as f:
    for sv in sinh_vien:
        f.write(sv + "\n")

print("Đã ghi xong")
