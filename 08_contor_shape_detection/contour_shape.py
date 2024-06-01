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

# step 3: Find the contours
contours, hierarchy = cv2.findContours(canny_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# step 4: Find length of the contours
print(f"Length of contours = {str(len(contours))}")

# step 5: Draw the contours
copy_main_image = image.copy()
cv2.drawContours(copy_main_image, contours, -1, (0, 255, 0), 3)


cv2.imshow('Original image', image)
cv2.imshow('Gray', gray_image)
cv2.imshow('Canny', canny_image)
cv2.imshow('Contours', copy_main_image)
cv2.waitKey(0)

