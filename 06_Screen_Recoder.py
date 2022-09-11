# Screen Recoder

import cv2
import pyautogui
import numpy as np

# create resolution
screenResolution = pyautogui.size()     # return screen width and height

# file name in which we want to store recording
fileName = input("Enter file name and path: ")

# Now fix the frame rate
fps = 30

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(fileName, fourcc, fps, screenResolution)

# create recording module
cv2.namedWindow("Live Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Recording", (640, 480))

while True:
    img = pyautogui.screenshot()
    f = np.array(img)

    f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)

    output.write(f)
    cv2.imshow("Live Recording", f)

    k = cv2.waitKey(1)

    if k == ord("q"):
        break

output.release()
cv2.destroyAllWindows()
