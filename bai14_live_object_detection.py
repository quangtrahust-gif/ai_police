import cv2

# Hàm xử lý frame
def process_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Vẽ contours và bounding box
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 300:  # Lọc bỏ nhiễu
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.putText(frame, f'Objects: {len([c for c in contours if cv2.contourArea(c) > 300])}', 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return frame

# Mở camera (thử với index 0, 1, 2,...)
cap = cv2.VideoCapture(2)

if not cap.isOpened():
    print("Không thể mở camera. Thoát.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không nhận được frame.")
        break  # break trong vòng lặp while

    processed = process_frame(frame)
    cv2.imshow('Object Detection', processed)

    # Thoát khi nhấn 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # break trong vòng lặp while

cap.release()
cv2.destroyAllWindows()