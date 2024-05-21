import cv2

image = cv2.imread('../images/documentscanner2.jpg')

edge = cv2.Canny(image, 400, 500)

cv2.imshow('image', image)
cv2.imshow('EDGE image', edge)
cv2.waitKey(0)
