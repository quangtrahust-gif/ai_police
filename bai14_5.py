# bai14_5.py
import cv2
import numpy as np

img = np.zeros((400, 400), dtype=np.uint8)
cv2.rectangle(img, (50,50), (150,150), 255, -1)
cv2.circle(img, (300, 100), 50, 255, -1)

contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

for cnt in contours:
    area = cv2.contourArea(cnt)
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(color_img, (x,y), (x+w,y+h), (255,0,0), 2)
    cv2.putText(color_img, f'Area: {area}', (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)

cv2.imshow('Bounding Boxes', color_img)
cv2.waitKey(0)
