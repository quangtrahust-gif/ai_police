# bai8_3.py
# Từ điển Anh - Việt đơn giản
tu_dien = {
    "hello": "xin chào",
    "goodbye": "tạm biệt",
    "love": "yêu thương"
}

while True:
    print("\n--- TỪ ĐIỂN ANH - VIỆT ---")
    tu = input("Nhập từ tiếng Anh (hoặc 'exit' để thoát): ").lower()
    if tu == "exit":
        break
    if tu in tu_dien:
        print(f"{tu} -> {tu_dien[tu]}")
    else:
        them = input(f"Chưa có từ '{tu}', bạn có muốn thêm? (y/n): ").lower()
        if them == 'y':
            nghia = input(f"Nhập nghĩa của '{tu}': ")
            tu_dien[tu] = nghia
            print("Đã thêm vào từ điển!")
        else:
            print("Hẹn gặp lại!")
