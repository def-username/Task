#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import cv2
def normalization(image,channel):
    mean=np.mean(image[:,:,channel])
    std=np.std(image[:,:,channel])
    image=(image-mean)/std
    return image

image=cv2.imread("E:\\Pictures\\IMG-20170120-WA0386.jpg")
new=normalization(image,0)
cv2.imshow("Image",new)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




