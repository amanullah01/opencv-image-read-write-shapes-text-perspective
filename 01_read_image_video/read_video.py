import cv2

video = cv2.VideoCapture("../videos/2.mp4")

while True:
    success, frame = video.read()

    if not success:
        break

    cv2.imshow('Read video from directory', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
