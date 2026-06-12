# bai9_2.py
try:
    with open("ds_sinh_vien.txt", "r", encoding="utf-8") as f:
        for dong in f:
            print(dong.strip())   # strip() bỏ ký tự xuống dòng
except FileNotFoundError:
    print("File không tồn tại!")
