import cv2

img = cv2.imread(r"C:\Machine_vision\Prelab\sample.jpeg")

if img is None:
    print("Image not found")
else:
    print("Image loaded successfully")
    print("Shape:", img.shape)