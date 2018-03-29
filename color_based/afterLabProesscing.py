from PIL import Image
import numpy
import pyopencl as cl

im=Image.open("DSC_0785.tiff")
im2=Image.open("shadow_removed_lab.tiff")
raw = im.load()
lab_result= im2.load()

width=im.size[0]
height=im.size[1]

test=Image.new("RGB",(width,height))
for i in range(width):
    for j in range(height):
        if(lab_result[i,j]==255):
              test.putdata(255,255,255)
        else:
            test.putdata(raw[i,j][0],raw[i,j][1],raw[i,j][2])
        
outname=im.filename+'shadowtest.tiff'
test.save(outname)