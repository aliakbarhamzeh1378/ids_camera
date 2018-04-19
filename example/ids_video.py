import numpy as np
import cv2
import ids
import ids_core

cam = ids.Camera()
cam.color_mode = ids_core.COLOR_RGB8
cam.exposure = 5
cam.auto_exposure = True
cam.continuous_capture = True
while True:


    img, meta = cam.next()
    a = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow("mask", a)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

