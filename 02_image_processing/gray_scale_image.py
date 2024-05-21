import cv2

image = cv2.imread('../images/car.jpg')
cv2.imshow('Original image', image)

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image', grayImage)

cv2.waitKey(0)
