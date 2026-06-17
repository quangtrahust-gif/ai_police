from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

# Mở video file
cap = cv2.VideoCapture(0)  # MYNT EYE thường ở index 4

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Chạy YOLO trên frame
    results = model(frame)

    # Vẽ kết quả
    annotated_frame = results[0].plot()

    cv2.imshow('YOLO Video Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
