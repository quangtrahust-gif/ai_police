import cv2
import numpy as np

# Tạo ảnh giả (hình tròn trắng trên nền đen)
img = np.zeros((300, 300), dtype=np.uint8)
cv2.circle(img, (150, 150), 80, 255, -1)  # tô trắng
cv2.imwrite('circle.png', img)

# Đọc ảnh
gray = cv2.imread('circle.png', cv2.IMREAD_GRAYSCALE)

# Ngưỡng đơn
ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Ngưỡng Otsu
ret, thresh2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('Original', gray)
cv2.imshow('Binary', thresh1)
cv2.imshow('Otsu', thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()
