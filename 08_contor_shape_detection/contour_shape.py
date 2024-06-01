import cv2
import numpy as np

image = cv2.imread('../images/shapes.png')
# image = cv2.imread('../images/main_dots.jpeg')

# step 1 => Convert the image into grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# step 2 => apply canny edge detector
lower_threshold = 100
upper_threshold = 150

canny_image = cv2.Canny(gray_image, lower_threshold, upper_threshold)

cv2.imshow('Original image', image)
cv2.imshow('Gray', gray_image)
cv2.imshow('Canny', canny_image)
cv2.waitKey(0)

