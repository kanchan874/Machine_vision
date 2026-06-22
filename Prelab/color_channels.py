import cv2

img = cv2.imread(r"C:\Machine_vision\Prelab\sample.jpeg")

if img is not None:
    blue = img[:, :, 0]
    green = img[:, :, 1]
    red = img[:, :, 2]

    print("Blue Channel Shape:", blue.shape)
    print("Green Channel Shape:", green.shape)
    print("Red Channel Shape:", red.shape)

    cv2.imwrite("blue_channel.jpg", blue)
    cv2.imwrite("green_channel.jpg", green)
    cv2.imwrite("red_channel.jpg", red)

    print("Channel images saved successfully")
else:
    print("Image not found")