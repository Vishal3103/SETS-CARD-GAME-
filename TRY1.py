import numpy as np
import cv2

image_src = cv2.imread("sets.jpg")

gray = cv2.cvtColor(image_src, cv2.COLOR_BGR2GRAY)
blur= cv2.pyrMeanShiftFiltering(image_src, 9,33)
ret, thresh = cv2.threshold(gray, 120, 250,0)


image, contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#mask = np.zeros(image_src.shape, np.uint8)


cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)
cv2.imshow('image',thresh)

cv2.drawContours(image_src,contours,0,(0,0,255),6)
cv2.namedWindow('contours',cv2.WINDOW_NORMAL)
cv2.resizeWindow('contours', 600,600)
cv2.imshow('contours',image_src)


mask = np.zeros(image_src.shape, np.uint8)
largest_areas = sorted(contours, key=cv2.contourArea)
cv2.drawContours(mask, [largest_areas[-2]], 0, (255,255,255,255), -1)
removed = cv2.add(image_src, mask)

cv2.imwrite("removed.png", removed)

cv2.waitKey(0)
cv2.destroyAllWindows()
