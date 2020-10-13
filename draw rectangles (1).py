#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import numpy
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame=cv2.resize(frame,(400,400))
    cv2.rectangle(frame,(0,0),(20,20),(255,0,0),3)
    cv2.rectangle(frame,(380,0),(400,20),(0,0,255),3)
    cv2.imshow('frame', frame)
    if 0xFF & cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:




