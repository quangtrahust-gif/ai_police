import cv2
import os
import time

# Tạo thư mục lưu ảnh
save_dir = "custom_dataset/images/raw"
os.makedirs(save_dir, exist_ok=True)

# Mở camera MYNT EYE (thử các index: 4, 0, 1, 2...)
cap = cv2.VideoCapture(4)
if not cap.isOpened():
    print("Không mở được camera index 4, thử index 0...")
    cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Không thể mở camera. Kiểm tra kết nối.")
    exit()

print("=== CHỤP ẢNH TẠO DATASET ===")
print("Nhấn 's' để chụp ảnh")
print("Nhấn 'q' để thoát")
print(f"Ảnh sẽ lưu vào: {save_dir}")

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Không đọc được frame.")
        break

    # Hiển thị hướng dẫn trên frame
    cv2.putText(frame, f"Anh: {count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow('MYNT EYE - Capture Dataset', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        timestamp = int(time.time())
        filename = f"{save_dir}/img_{timestamp}_{count:04d}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Đã lưu: {filename}")
        count += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"Hoàn tất! Đã chụp {count} ảnh.")