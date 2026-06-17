# bai14_4.py
import cv2
import numpy as np

# Tạo ảnh có nhiều hình
img = np.zeros((400, 400), dtype=np.uint8)
cv2.rectangle(img, (50,50), (150,150), 255, -1)
cv2.circle(img, (300, 100), 50, 255, -1)
cv2.ellipse(img, (200, 300), (60, 40), 0, 0, 360, 255, -1)

# Tìm contours
contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Tạo ảnh màu để vẽ
color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(color_img, contours, -1, (0,255,0), 3)

cv2.imshow('Contours', color_img)
cv2.waitKey(0)
