#capture picture from camera

import cv2
import time
cam=cv2.VideoCapture(0)
#0 for inbuilt camera

time.sleep(1)

_,img=cam.read()
cv2.imwrite("imagefromcam.jpg",img)
cam.release()
cv2.destroyAllWindow()


