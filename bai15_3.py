from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

# Mở camera (thử các index: 0, 1, 2, 3, 4...)
cap = cv2.VideoCapture(0)  # MYNT EYE thường ở index 4

if not cap.isOpened():
    print("Không mở được camera. Thử index khác.")
    exit()

print("Nhấn 'q' để thoát")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Chạy YOLO
    results = model(frame)

    # Vẽ kết quả
    annotated_frame = results[0].plot()

    # Thêm thông tin FPS (ước lượng)
    cv2.putText(annotated_frame, 'YOLOv8 - MYNT EYE', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow('YOLO Real-time Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
