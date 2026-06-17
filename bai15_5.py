# bai15_5.py
from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

img = cv2.imread('sample.jpg')

# Chạy với ngưỡng confidence 0.5 (chỉ lấy kết quả có độ tin cậy >= 50%)
results = model(img, conf=0.5)

annotated_img = results[0].plot()
cv2.imshow('YOLO - Confidence >= 0.5', annotated_img)
cv2.waitKey(0)
