import cv2
import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)


image = cv2.imread("../images/face.png")
cv2.imshow("Read Image from Directory", image)
cv2.waitKey(0)
