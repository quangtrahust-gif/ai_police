# bai14_6.py
import cv2

# Đọc ảnh chứa nhiều vật thể (ví dụ ảnh biển báo, sản phẩm...)
img = cv2.imread('sample.jpg')
if img is None:
    print("Dùng ảnh mẫu sample.jpg")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)

# Ngưỡng Otsu để tách vật thể
_, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Tìm contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Lọc các contours nhỏ (nhiễu)
valid_contours = [c for c in contours if cv2.contourArea(c) > 100]

# Vẽ và đánh số
for i, cnt in enumerate(valid_contours):
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.putText(img, str(i+1), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)

cv2.putText(img, f'Count: {len(valid_contours)}', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

cv2.imshow('Object Counting', img)
cv2.waitKey(0)
