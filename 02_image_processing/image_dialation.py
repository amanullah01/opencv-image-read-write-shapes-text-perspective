import cv2
import numpy as np

image = cv2.imread('../images/documentscanner2.jpg')

kernel = np.ones((5, 5), np.uint8)


cannyEdge = cv2.Canny(image, 400, 500)

dilateImage = cv2.dilate(cannyEdge, kernel, iterations=1)

cv2.imshow('image', image)
cv2.imshow('EDGE image', cannyEdge)
cv2.imshow('Dilate image', dilateImage)
cv2.waitKey(0)
