from ultralytics import YOLO
import cv2

# Tải mô hình YOLOv8 pre-trained (sẽ tự động download lần đầu)
model = YOLO('yolov8n.pt')  # 'n' là nano - nhẹ và nhanh

# Đọc ảnh
img = cv2.imread('sample.jpg')
resized = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
if img is None:
    print("Không tìm thấy ảnh. Hãy tạo một ảnh mẫu hoặc dùng camera.")
    exit()

# Chạy inference
results = model(resized)

# Vẽ kết quả lên ảnh
annotated_img = results[0].plot()

# Hiển thị
cv2.imshow('YOLO Detection', annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()