import cv2
import numpy as np

image = cv2.imread('../images/cards.jpg')

width, height = 500, 500

pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
outputImage = cv2.warpPerspective(image, matrix, (width, height))
cv2.imshow('Original image', image)
cv2.imshow('Warp Perspective image', outputImage)
cv2.waitKey(0)
