import cv2
import numpy as np

# create an image
image = np.zeros((512, 512, 3), np.uint8)
# fill blue color
image[:] = 255, 0, 0

cv2.line(image, (0, 0), (image.shape[1], image.shape[0]), (0, 255, 0), 5)

cv2.rectangle(image, (0, 0), (256, 256), (0, 0, 255), 3)

cv2.circle(image, (380, 150), 100, (0, 255, 140), -1)

cv2.putText(image, "Open CV Shapes", (280, 20), cv2.FONT_HERSHEY_PLAIN, 1, (189, 160, 240), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)
