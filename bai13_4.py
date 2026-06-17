import cv2
import numpy as np

cap = cv2.VideoCapture(3)
if not cap.isOpened():
    exit()

ret, frame = cap.read()
if ret:
    # Vẽ hình chữ nhật
    cv2.rectangle(frame, (100, 100), (200, 200), (255, 0, 0), 2)
    # Vẽ hình tròn
    cv2.circle(frame, (300, 150), 50, (0, 0, 255), -1)
    # Vẽ đường thẳng
    cv2.line(frame, (50, 50), (400, 300), (0, 255, 0), 3)
    # Viết chữ
    cv2.putText(frame, 'MYNT EYE', (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

    cv2.imshow('Drawing', frame)
    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()