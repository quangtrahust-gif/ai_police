# bai5_5.py
mat_khau_dung = "python123"
so_lan_nhap = 0
while so_lan_nhap < 3:
    mk = input("Nhập mật khẩu: ")
    if mk == mat_khau_dung:
        print("Đăng nhập thành công!")
        break
    else:
        so_lan_nhap += 1
        print(f"Sai mật khẩu. Còn {3 - so_lan_nhap} lần thử.")
else:
    print("Bạn đã nhập sai quá 3 lần. Tài khoản bị khóa.")
