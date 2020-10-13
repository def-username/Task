#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import numpy as np
def combine_images_v(img1,img2):
    print(img1.shape)
    print(img2.shape)
    img1=cv2.resize(img1,(960,1280),None,.5,.5)
    img2=cv2.resize(img2,(960,1280),None,.5,.5)
    verr=np.vstack((img1,img2))
    cv2.imshow("Vertical",ver)
img1=cv2.imread("E:\\Pictures\\IMG-20170120-WA0386.jpg")
img2=cv2.imread("E:\\Pictures\\IMG-20170911-WA0032.jpg")
combine_images_v(img1,img2)
cv2.waitKey(0)
cv2.destroyAllWindows  


# In[ ]:




