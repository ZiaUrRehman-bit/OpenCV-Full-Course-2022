import cv2

# 1. read video
cap = cv2.VideoCapture("traffic.avi")

# now what is in cap, let's see
print('cap:', cap)  # so basically cap is an object of video capture

# as video is collection of frames
while True:

    status, frame = cap.read()    # status return boolean value True for read frame successfully, false for not

    # 2. resize the frame
    frame = cv2.resize(frame, (700, 500))

    # 3. convert frames into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frames", frame)

    # showing gray frames
    cv2.imshow("gray frames", gray)

    # waits untill q pressed
    k = cv2.waitKey(100)
    if k == ord('q'):   # if not work the write k == ord('q') & 0xFF: this is mask
        break

cap.release() # relase the cap which capture the video
cv2.destroyAllWindows()


