# bai14_2.py
import cv2

# Đọc ảnh (có thể dùng ảnh từ camera hoặc file)
img = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Không có ảnh mẫu, dùng ảnh giả")
    img = cv2.imread('circle.png', cv2.IMREAD_GRAYSCALE)

# Ngưỡng thích nghi
thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Adaptive Threshold', thresh)
cv2.waitKey(0)
