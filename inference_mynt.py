from ultralytics import YOLO
import cv2

# Tải mô hình đã huấn luyện
model = YOLO('best.pt')

# Mở camera MYNT EYE (thử index 4, 0, 2...)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Không tìm thấy camera.")
        exit()

print("Nhấn 'q' để thoát")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Chạy inference trên CPU
    results = model(frame, device='cpu', conf=0.45)

    # Vẽ kết quả lên frame
    annotated = results[0].plot()

    # Thêm thông tin FPS (ước lượng nếu muốn)
    cv2.putText(annotated, "Model: cup detection", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow('MYNT EYE - Cup Detection', annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
