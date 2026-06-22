import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam not found")
else:
    print("Webcam opened successfully")

cap.release()