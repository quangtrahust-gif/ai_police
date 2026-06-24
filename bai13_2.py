import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Không mở được camera")
    exit()

ret, frame = cap.read()
if ret:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('mynt_gray.jpg', gray)
    cv2.imshow('MYNT Gray', gray)
    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()