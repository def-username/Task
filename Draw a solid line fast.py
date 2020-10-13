#!/usr/bin/env python
# coding: utf-8

# In[8]:



import cv2
def draw_solid_square_fast(image, x, y, l, color):
    image = cv2.line(image,(x,y),(x+l,y),color,10)
    image = cv2.line(image,(x+l,y),(x+l,y+l),color,10)
    image = cv2.line(image,(x+l,y+l),(x,y+l),color,10)
    image = cv2.line(image,(x,y+l),(x,y),color,10)
    return image
image = cv2.imread("E:\\Pictures\\IMG-20170120-WA0386.jpg")
draw_solid_square_fast(image,0,0,500,(0,255,0))
cv2.imshow('100', image)
cv2.waitKey(0)
cv2.destroyAllWindows  


# In[ ]:




