from PIL import Image
import numpy
from scipy.stats.stats import pearsonr

im = Image.open("DSC_0795.NEF") 

pix = im.load()

width=im.size[0]
height=im.size[1]

# find where pure background section on the left of the image
cor_result=[]
for i in range(width):
    if i<width-1:
        left=[]
        right=[]
        for j in range(height):
            left.append(sum(pix[i,j]))
            right.append(sum(pix[i+1,j]))
        
        cor_result.append(pearsonr(left,right))

left = 11
top = 1
right = 138
bottom = height
cropped_example = im.crop((left, top, right, bottom))

#for i in range(pearsonr):
#    if i