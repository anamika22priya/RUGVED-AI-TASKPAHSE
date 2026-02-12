import cv2 as cv
import numpy as np

cap = cv.VideoCapture("files/Ball_Tracking.mp4")

trajectory = []

while cap.isOpened():
    isTrue, frame = cap.read()
    
    if not isTrue:
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_green = np.array([40, 140, 140])
    upper_green = np.array([60, 200, 200])

    mask = cv.inRange(hsv, lower_green, upper_green)

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    if contours:
            c = max(contours, key=cv.contourArea)
            
            (x, y), radius = cv.minEnclosingCircle(c)
            center = (int(x), int(y))
            trajectory.append(center)
            
            cv.circle(frame, center, int(radius), (0, 255, 0), 2)
            cv.circle(frame, center, 5, (255, 0, 0), -1)


    for i in range(1, len(trajectory)):
        cv.line(frame, trajectory[i-1], trajectory[i], (0, 0, 255), 2)

    cv.imshow("Green Ball Tracking", frame)

    if cv.waitKey(10)& 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
