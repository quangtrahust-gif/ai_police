# bai14_3.py
import cv2

img = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    img = cv2.imread('circle.png', cv2.IMREAD_GRAYSCALE)

# Làm mờ để giảm nhiễu
blurred = cv2.GaussianBlur(img, (5,5), 0)

# Canny
edges = cv2.Canny(blurred, 50, 150)

cv2.imshow('Original', img)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
