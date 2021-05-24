from djitellopy import tello
import cv2
import numpy as np

frameWidth = 480
frameHeight = 360

#me = tello.Tello()
#me.connect()
#print(me.get_battery())
#me.streamon()

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

cap = cv2.VideoCapture()
frameCounter = 0

while True:

    #img = me.get_frame_read().frame

    _, img = cap.read()

    img = cv2.resize(img, (480, 360))
    img = cv2.flip(img, 0)
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE min", "HSV")
    h_max = cv2.getTrackbarPos("HUE max", "HSV")
    s_min = cv2.getTrackbarPos("SAT min", "HSV")
    s_max = cv2.getTrackbarPos("SAT max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE max", "HSV")

    lower = np.array(h_min, s_min, v_min)
    upper = np.array(h_max, s_max, v_max)
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    print(f'[{h_min},{s_min},{v_min},{h_max},{s_max},{v_max}]')

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()