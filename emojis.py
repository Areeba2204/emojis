#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2 as cv
import numpy as np


# In[9]:


b = np.zeros((400,400,3), np.uint8)
cir=cv.circle(b,(100,200), 63, (155,220,255), -1)
line= cv.line(b,(70,170),(85,172),(205,100,200),5)
line= cv.line(b,(115,170),(130,172),(205,100,200),5)
line= cv.line(b,(80,215),(120,215),(205,100,200),5)
text=cv.putText(b,"disgused",(30,350),2,cv.FONT_HERSHEY_COMPLEX,(135,200,200),3)
cv.imshow('emoji', b)
cv.waitKey(0)


# In[10]:


bl = np.zeros((400,400,3), np.uint8)
cir=cv.circle(bl,(200,200), 70, (200,220,255), -1)
cir=cv.circle(bl,(170,180), 6, (155,100,215), -1)
cir=cv.circle(bl,(220,180), 6, (155,100,215), -1)
el=cv.ellipse(bl,(200,220),(40,30),0,0,180,120,-1)
text=cv.putText(bl,"happy",(30,350),4,cv.FONT_HERSHEY_COMPLEX,(220,210,244),3)
cv.imshow('emoji', bl)
cv.waitKey(0)


# In[ ]:




