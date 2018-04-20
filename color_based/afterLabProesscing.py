from PIL import Image
import numpy as np
import pyopencl as cl

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

masked={}
for i in range(width):
    this_masked=[]
    for j in range(height):
        if(lab_result[i,j]==255):
            this_masked.append(j)
    masked[i]=this_masked        
