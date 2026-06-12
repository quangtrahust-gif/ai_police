# bai9_4.py
# Giả sử file diem.txt có nội dung:
# An,8.5
# Binh,7.0
# Chi,9.0

try:
    with open("diem.txt", "r", encoding="utf-8") as f:
        for dong in f:
            dong = dong.strip()
            if dong:
                ten, diem = dong.split(",")
                print(f"Sinh viên {ten} được {diem} điểm")
except FileNotFoundError:
    print("File diem.txt chưa tồn tại. Hãy tạo file trước.")
