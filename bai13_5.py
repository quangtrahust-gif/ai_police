import cv2

# Thay index bằng số tìm được ở bước 2
cap = cv2.VideoCapture(0)   # Giả sử index = 2  

if not cap.isOpened():
    print("Không mở được camera")
    exit()

print("Nhấn 'q' để thoát")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không đọc được frame, kiểm tra camera")
        break

    cv2.imshow('MYNT EYE Live', frame)

    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()