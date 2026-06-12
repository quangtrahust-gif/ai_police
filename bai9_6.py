# bai9_6.py
def sao_chep_file(nguon, dich):
    try:
        with open(nguon, "r", encoding="utf-8") as f_nguon:
            noi_dung = f_nguon.read()
        with open(dich, "w", encoding="utf-8") as f_dich:
            f_dich.write(noi_dung)
        print(f"Đã sao chép từ {nguon} sang {dich}")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {nguon}")
    except Exception as e:
        print(f"Lỗi: {e}")

sao_chep_file("ds_sinh_vien.txt", "ds_sinh_vien_backup.txt")
