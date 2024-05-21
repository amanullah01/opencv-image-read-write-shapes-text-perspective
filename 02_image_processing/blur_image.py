import cv2

image = cv2.imread('../images/car.jpg')
blur = cv2.GaussianBlur(image, (35, 35), 0)
cv2.imshow('Original Image', image)
cv2.imshow('Blur Image', blur)
cv2.waitKey(0)
