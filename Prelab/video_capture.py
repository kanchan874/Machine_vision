
import cv2

cap = cv2.VideoCapture(r"C:\Machine_vision\Prelab\sample.mp4")

if not cap.isOpened():
    print("Video file not found!")
else:
    print("Video opened successfully")

cap.release()