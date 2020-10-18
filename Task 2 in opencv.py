#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
def nothing(x):
    pass  

cap = cv2.VideoCapture(0)
cv2.namedWindow("Frames")
cv2.createTrackbar("Min-H","Frames",0,180,nothing)
cv2.createTrackbar("Min-S","Frames",0,255,nothing)
cv2.createTrackbar("Min-V","Frames",0,255,nothing)
cv2.createTrackbar("Max-H","Frames",180,180,nothing)
cv2.createTrackbar("Max-S","Frames",255,255,nothing)
cv2.createTrackbar("Max-V","Frames",255,255,nothing)
cv2.setTrackbarPos("Min-H","Frames",104)
cv2.setTrackbarPos("Min-S","Frames",169)
cv2.setTrackbarPos("Min-V","Frames",0)
cv2.setTrackbarPos("Max-H","Frames",151)
cv2.setTrackbarPos("Max-S","Frames",255)
cv2.setTrackbarPos("Max-V","Frames",213)
x=False
while True:
    _,frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
    l_h=cv2.getTrackbarPos("Min-H","Frames")
    l_s=cv2.getTrackbarPos("Min-S","Frames")
    l_v=cv2.getTrackbarPos("Min-V","Frames")
    
    u_h=cv2.getTrackbarPos("Max-H","Frames")
    u_s=cv2.getTrackbarPos("Max-S","Frames")
    u_v=cv2.getTrackbarPos("Max-V","Frames")
    
    low_magenta=np.array([l_h, l_s, l_v])
    high_magenta=np.array([u_h, u_s, u_v])
    magenta_mask=cv2.inRange(hsv_frame, low_magenta,high_magenta)
    magenta = cv2.bitwise_and(frame, frame, mask=magenta_mask)
    
    low_blue = np.array([l_h, l_s, l_v])
    high_blue = np.array([u_h, u_s, u_v])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
   
    low_green = np.array([47, 47, 121])
    high_green = np.array([94, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    
    low_y = np.array([0, 51, 180])
    high_y = np.array([31, 255, 255])
    y_mask = cv2.inRange(hsv_frame, low_y, high_y)
    yellow = cv2.bitwise_and(frame, frame, mask=y_mask)

    cv2.imshow('yellow', yellow)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
   # elif cv2.waitKey(1) == ord ('b'):
       # global x
       # x=True
       # while (x):
        #    cv2.imshow("blue",blue)
cap.release()
cv2.destroyAllWindows()


# In[ ]:




