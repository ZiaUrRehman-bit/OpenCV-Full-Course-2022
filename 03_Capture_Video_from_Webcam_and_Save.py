
# Capture video from webcam and save in to memory

import cv2

cap = cv2.VideoCapture(0)  # 0 for webcam
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # if warning shows in terminal window its version problem

# 2 how we save so we have to create an output object

# DIVX, XVID, MJPG, X264, video formates
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # it helps video writer to select the format in which you want to store
# output is an object
# It contains 4 parameter name of output video, formate in the form of codec, fps, resolution
output = cv2.VideoWriter("ouput.avi", fourcc, 20, (640, 480))

# output = cv2.VideoWriter("ouput.avi", fourcc, 20, (640, 480),0 ) # this 0 is added at end for storing grayscale video

# 2 above

while True:
    Success, frame = cap.read()   # Success is true if frame read successfully

    if Success == True:

        cv2.imshow("Webcam", frame)

        # save
        output.write(frame)

        k = cv2.waitKey(1)
        if k == ord('q'):
            break

# You have to release both objects and memory
cap.release()
output.release()
cv2.destroyAllWindows()