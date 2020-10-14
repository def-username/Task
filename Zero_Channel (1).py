#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import numpy as np
def zero_channel(image, channel):
    image[:,:,channel]=np.zeros(np.shape(image[:,:,channel]),dtype=np.uint8)
    return image
image = cv2.imread("E:\\Pictures\\20190101_005848.jpg")
cv2.imshow("IMAGE",zero_channel(image,1))
cv2.waitKey(0)
cv2.destroyAllWindows


# In[ ]:





# In[ ]:



       


# In[ ]:





# In[14]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[43]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[53]:



    


# In[ ]:





# In[ ]:




