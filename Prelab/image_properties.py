import cv2

img = cv2.imread(r"C:\Machine_vision\Prelab\sample.jpeg")

if img is not None:
    print("Shape:", img.shape)
    print("Height:", img.shape[0])
    print("Width:", img.shape[1])
    print("Channels:", img.shape[2])
else:
    print("Image not found")