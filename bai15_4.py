from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

img = cv2.imread('sample.jpg')
results = model(img)

# Lấy kết quả từ frame đầu tiên
result = results[0]

# Danh sách các đối tượng phát hiện được
boxes = result.boxes  # Box object
for box in boxes:
    # Tọa độ bounding box
    x1, y1, x2, y2 = box.xyxy[0].tolist()
    # Độ tin cậy (confidence)
    conf = box.conf[0].item()
    # Lớp đối tượng (class ID)
    cls_id = int(box.cls[0].item())
    # Tên lớp
    cls_name = result.names[cls_id]

    print(f"Đối tượng: {cls_name}, Độ tin cậy: {conf:.2f}, Vị trí: ({x1:.0f}, {y1:.0f}) - ({x2:.0f}, {y2:.0f})")

# Hiển thị ảnh đã được vẽ
annotated_img = result.plot()
cv2.imshow('YOLO with Info', annotated_img)
cv2.waitKey(0)
