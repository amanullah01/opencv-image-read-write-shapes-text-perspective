import numpy as np
import cv2

# image size and color channel should be same to join
image1 = cv2.imread('../images/cards.jpg')
print(image1.shape)

image2 = cv2.imread('../images/car.jpg')
print(image2.shape)
image2_resize = cv2.resize(image2, (477, 500))

horizontal_stack = np.hstack((image1, image2_resize))
vertical_stack = np.vstack((image1, image2_resize))

cv2.imshow('horizontal_stack', horizontal_stack)
cv2.imshow('vertical_stack', vertical_stack)
cv2.waitKey(0)


