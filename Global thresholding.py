#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import cv2
def thres_finder(img, thres=20,delta_T=1.0):
    
    # Step-2: Divide the images in two parts
    x_low, y_low = np.where(img<=thres)
    x_high, y_high = np.where(img>thres)
    
    # Step-3: Find the mean of two parts
    mean_low = np.mean(img[x_low,y_low])
    mean_high = np.mean(img[x_high,y_high])
    
    # Step-4: Calculate the new threshold
    new_thres = (mean_low + mean_high)/2
    
    # Step-5: Stopping criteria, otherwise iterate
    if abs(new_thres-thres)< delta_T:
        return new_thres
    else:
        return thres_finder(img, thres=new_thres,delta_T=1.0)
img = cv2.imread("D:\\Univ\\Torpedo\\cv\\Computer-Vision-main\\Computer-Vision-main\\lecture_3\\eren.png",cv2.IMREAD_GRAYSCALE)
vv1 = thres_finder(img, thres=20,delta_T=1.0)
ret, thresh = cv2.threshold(img,vv1,255,cv2.THRESH_BINARY)
out = cv2.hconcat([img,thresh])
cv2.imshow('threshold',out)
print(ret)
cv2.waitKey(0)


# In[ ]:




