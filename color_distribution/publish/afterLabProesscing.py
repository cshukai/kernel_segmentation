from PIL import Image
import numpy as np
import pyopencl as cl
import cv2

im=Image.open("DSC_0785.tiff")
im2=Image.open("shadow_removed_lab.tiff")
raw = im.load()
lab_result= im2.load()

width=im.size[0]
height=im.size[1]

test=Image.new(im.mode, im.size)

#confirmed that no overlap between shadow and mask
pixels=test.load()
for i in range(width):
    for j in range(height):
        if(lab_result[i,j]==255):
            pixels[i,j]=(255,255,255)
        else:
            pixels[i,j]=raw[i,j]

       
outname=im.filename+'shadowtest.tiff'
test.save(outname)

#exisiting contour finder
im3=cv2.imread('shadow_removed_lab.tiff',0)
im6=cv2.imread('DSC_0785.tiff')
#_, contours, hierc = cv2.findContours(im3,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) 
_, contours, hierc = cv2.findContours(im3,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)



im4=im3.copy()
itr=0
for cnt in contours:
    
    (x,y,w,h) = cv2.boundingRect(cnt)
    #im5=cv2.rectangle(im4,(x,y),(x+w,y+h),(0,255,0),2)
    kernel = im6[y:y+h,x:x+w]
    #cv2.imwrite(str(itr)+'.png',kernel)
    cv2.imwrite(str(itr)+'.tiff',kernel)
    itr=itr+1
#alignment - gpu
masked={}
for i in range(width):
    this_masked=[]
    for j in range(height):
        if(lab_result[i,j]==255):
            this_masked.append(j)
    if(len(this_masked)>1):
     masked[i]=this_masked        

allKeys=masked.keys()