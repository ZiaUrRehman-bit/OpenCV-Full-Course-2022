# extracting the frames from video

import cv2

cam = cv2.VideoCapture("traffic.avi")
Success, frame = cam.read()
count = 0

while True:
    if Success:
        cv2.imwrite(f"frames\\imgn{count}.jpg", frame)

        # setting the frame speed
        cam.set(cv2.CAP_PROP_POS_MSEC, (count**100))

        Success, frame = cam.read()

        cv2.imshow("frame extraction", frame)

        count +=1
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
            cv2.destroyAllWindows()

cam.release()
cv2.destroyAllWindows()