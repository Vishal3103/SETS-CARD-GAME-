import cv2
import numpy as np

im = cv2.imread('sets2.jpg')

Mat mask
// specify the range of colours that you want to include, you can play with the borders here if you like
cv::Scalar lowerb = cv::Scalar(255,127,39)
cv::Scalar upperb = cv::Scalar(255,127,39)

cv::inRange(frame, lowerb, upperb, mask)

imshow("mask", mask); 
