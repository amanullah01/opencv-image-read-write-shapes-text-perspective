import cv2

image = cv2.imread('../images/image3.png')
print("Original Image shape: ", image.shape)

# first parameter is height, second parameter is width
cropped_image = image[0:100, 200:500]
print("Cropped Image shape: ", cropped_image.shape)

cv2.imshow('Original image', image)
cv2.imshow('Cropped image', cropped_image)
cv2.waitKey(0)
