import numpy as np
import cv2
from matplotlib import pyplot as plt
# 40, 41, 48 similar
img1 = cv2.imread('40.tiff',1)          # queryImage
img2 = cv2.imread('41.tiff',1) # trainImage


# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create() 
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)