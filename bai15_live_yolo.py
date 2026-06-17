from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)  # Thay index nếu cần
if not cap.isOpened():
    print("Không mở được camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    # Đếm số người (class ID = 0)
    person_count = 0
    for box in results[0].boxes:
        cls_id = int(box.cls[0].item())
        if cls_id == 0:  # person
            person_count += 1

    # Vẽ kết quả
    annotated_frame = results[0].plot()

    # Hiển thị số lượng người
    cv2.putText(annotated_frame, f'People: {person_count}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('YOLO - People Counter', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
