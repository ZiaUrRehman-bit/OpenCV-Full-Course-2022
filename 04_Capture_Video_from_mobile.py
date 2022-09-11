
# Capture video from mobile app
# Download app iriun Webcam app from play store into your mobile
# Also download software iriun for windows into your laptop

import cv2

cam = cv2.VideoCapture(1)

while True:
    Success, Frame = cam.read()

    cv2.imshow("Mobile Cam", Frame)
    k = cv2.waitKey(1)

    if k == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()