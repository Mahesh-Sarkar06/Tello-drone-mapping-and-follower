from djitellopy import tello
import time
import cv2
import keyControl as kc
import numpy as np
import math

### PARAMETERS ###
fspd = 117 / 10  # in cm/s (15 cm/s)
aspd = 360 / 10  # in deg/s
interval = 0.25

dInterval = fspd * interval
aInterval = aspd * interval
##################

x, y = 500, 500
a = 0
yaw = 0

kc.init()
me = tello.Tello()
# me.connect()
# print(me.get_battery())
points = [(0, 0), (0, 0)]
# me.takeoff()

### left-right, forward-backward, up-down, yaw
# me.send_rc_control(0, 50, 0, 0)   ### forward
# sleep(2)
# me.send_rc_control(30, 0, 0, 0)   ### right
# sleep(2)
# me.send_rc_control(0, 0, 0, 90)   ### Yaw
# sleep(2)
# me.send_rc_control(0, 0, 0, 0)
# me.land()

### Image
# me.streamon()
global img


### Keyboard Input
def getkeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    spd = 50
    d = 0
    global yaw, x, y, a

    if kc.getKey("LEFT"):
        lr = -spd
        d = dInterval
        a = -180
    elif kc.getKey("RIGHT"):
        lr = spd
        d = -dInterval
        a = 180

    if kc.getKey("UP"):
        fb = spd
        d = dInterval
        a = 270
    elif kc.getKey("DOWN"):
        fb = -spd
        d = -dInterval
        a = -90

    if kc.getKey("w"):
        ud = spd
    elif kc.getKey("s"):
        ud = -spd

    if kc.getKey("a"):
        yv = -spd
        yaw -= aInterval
    elif kc.getKey("d"):
        yv = spd
        yaw += aInterval

    # if kc.getKey("l"): me.land(); time.sleep(3)
    # if kc.getKey("t"): me.takeoff()
    time.sleep(interval - 0.12)  ### Make the movement of dot slower
    a += yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    # if kc.getKey("c"):
    #   cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
    #  time.sleep(0.3)
    return [lr, fb, ud, yv, x, y]


def drawPoints(img, points):
    for pts in points:
        cv2.circle(img, pts, 5, (0, 0, 255), cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0] - 500) / 100}, {(points[-1][1] - 500) / 100})m',
                (points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)


while True:
    val = getkeyboardInput()
    # me.send_rc_control(val[0], val[1], val[2], val[3])
    # img = me.get_frame_read().frame
    # img = cv2.resize(img, (360,240))
    # cv2.imshow("Image", img)
    #cv2.waitKey(1)

    img = np.zeros((1000, 1000, 3), np.uint8)
    if points[-1][0] != val[4] or points[-1][1] != val[5]:
        points.append((val[4], val[5]))
    drawPoints(img, points)
    cv2.imshow("Output", img)
    #time.sleep(1)
    print(val)
