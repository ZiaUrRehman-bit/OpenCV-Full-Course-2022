
# OpenCV: Open Source Computer Vision library to implement image processing

# In openCV we use arrays to store an image
# and Numpy library is used to handle arrays
# image always store in 2D array

# Images types
# Gray scale Image: Single channel
# True Color Image: RGB, BGR in Python, 3 channel
# Binary Image: 1 bit, 0 or 1 black or white

# Functions for Images in Python

import cv2    # OpenCV used as cv2 in python

# read an image and display

path = "C:\\Users\\hp\\Google Drive\\R&D\\Python\\" \
       "Machine_Learning\\OpenCV Full Course 2022\\pictures\\coloredChips.png"

img = cv2.imread(path)  # took path and name of image as an argument
print(img)
cv2.imshow("Image", img)
#cv2.waitKey()

# resize image
img_new = cv2.resize(img, (200, 200))
cv2.imshow("Resized Image", img_new)

# read image in grayscale
img1 = cv2.imread(path, 0)  # 0 means in grayscale
cv2.imshow("Image1", img1)

# flip the image
img = cv2.imread(path)
cv2.imshow("fliped image", cv2.flip(img, 1))  # it take parameters 0,-1,1

# Convert image to grayscale and save in current directory
img2 = cv2.imread(path, 0)  # 0 means in grayscale
cv2.imshow("Image2", img2)

k = cv2.waitKey()  # waits untill key press or wait for particular miliseocds time
if k == ord('s'):
       cv2.imwrite('output.png', img2)
else:
       cv2.destroyAllWindows()

# cv2.waitKey()
# cv2.destroyAllWindows()  # relase memory which used to store images

