import cv2

cap = cv2.VideoCapture(3) # Mở camera MYNT EYE (index 3)
if not cap.isOpened():
    exit()

ret, frame = cap.read()
if ret:
    # Resize xuống 50%
    resized = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    # Xoay 90 độ
    rotated = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    cv2.imshow('Original', frame)
    cv2.imshow('Resized', resized)
    cv2.imshow('Rotated', rotated)
    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()