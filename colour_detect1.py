import cv2
import numpy as np

img = cv2.imread("card_1.jpg")
BLUE_MIN = np.array([130, 0, 0], np.uint8)
BLUE_MAX = np.array([145, 100, 100], np.uint8)

dst = cv2.inRange(img, BLUE_MIN, BLUE_MAX)
no_blue = cv2.countNonZero(dst)
print('The number of blue pixels is: ' + str(no_blue))
cv2.namedWindow("opencv")
cv2.imshow("opencv",img)
cv2.waitKey(0)
