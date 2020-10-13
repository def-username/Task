#!/usr/bin/env python
# coding: utf-8

# In[13]:


import cv2
import numpy as np
def BGR2GRAY(image):
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("image",gray)
    return gray
image = cv2.imread("E:\\Pictures\\IMG-20170120-WA0386.jpg")
BGR2GRAY(image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




