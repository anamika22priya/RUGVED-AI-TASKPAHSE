import cv2 as cv
import numpy as np

cap = cv.VideoCapture("files/Ball_Tracking.mp4")

while cap.isOpened():
    isTrue, frame = cap.read()
    if not isTrue:
        break

    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Green color range
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([60, 200, 200])

    mask = cv.inRange(hsv, lower_green, upper_green)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv.erode(mask, kernel, iterations=1)
    mask = cv.dilate(mask, kernel, iterations=2)

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        c = max(contours, key=cv.contourArea)

        (x, y), radius = cv.minEnclosingCircle(c)
        center = (int(x), int(y))
        cv.circle(frame, center, int(radius), (0, 255, 0), 2)

    cv.imshow("Green Ball Tracking", frame)

    if cv.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
