import cv2

image = cv2.imread('../images/image.jpg')
print("Original Image shape: ", image.shape)

resize_image = cv2.resize(image, (1000, 650))
print("Resized Image shape: ", resize_image.shape)

cv2.imshow('Original image', image)
cv2.imshow('Resize image', resize_image)
cv2.waitKey(0)
