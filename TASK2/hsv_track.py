import cv2 as cv

cap = cv.VideoCapture('files/Ball_Tracking.mp4')  # change path
hsv = None

def show_hsv(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(hsv[y, x])   # prints HSV value

cv.namedWindow('Video')
cv.setMouseCallback('Video', show_hsv)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imshow('Video', frame)

    if cv.waitKey(100) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()
