import cv2

# Mở camera MYNT EYE (index 2)
cap = cv2.VideoCapture(2)

if not cap.isOpened():
    print("Không thể mở camera MYNT EYE. Kiểm tra kết nối.")
    exit()

# Đọc một frame để lấy ảnh
ret, frame = cap.read()
if ret:
    cv2.imshow('MYNT EYE - Frame', frame)
    cv2.waitKey(0)
else:
    print("Không đọc được frame.")

cap.release()
cv2.destroyAllWindows()