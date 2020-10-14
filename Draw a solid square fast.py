#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import numpy as np
def draw_solid_square_fast(image,x,y,l):
    image[x:x+l,[y,y+l]]=np.array([255,0,0])
    image[[x,x+l],y:y+l]=np.array([255,0,0])
image = cv2.imread("E:\\Pictures\\IMG-20170120-WA0386.jpg")
draw_solid_square_fast(image,0,0,500)
cv2.imshow('100', image)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[ ]:




