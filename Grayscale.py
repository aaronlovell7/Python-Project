#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:28:22 2019

@author: ericeun
"""

def grayscale():
    import cv2
    import numpy as np
    img = cv2.imread("Sample2.jpg")# Reading color image
    grayscale_image = 0.2126*img[:,:,2] + 0.7152*img[:, :,1] + 0.0722*img[:,:,0] #coresspnds to RGB and multiply the values  
    grayscale_image=grayscale_image.astype(np.uint8)
    cv2.imshow('Original image',img)#shows the original image
    cv2.imshow('Modified image',grayscale_image)#shows the grayscale image
    cv2.waitKey(0)
    cv2.destroyAllWindows()#destorys the window 

grayscale()
