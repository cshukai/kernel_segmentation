from PIL import Image
import numpy
from scipy.stats.stats import pearsonr

im = Image.open("DSC_0604.NEF") 

pix = im.load()

width=im.size[0]
height=im.size[1]

# find where pure background section on the left of the image
for i in range(width):
    if i<width-1:
        left=[]
        right=[]
        for j in range(height):
            left.append(sum(pix[i,j]))
            right.append(sum(pix[i+1,j]))
        
        pearsonr(left,right)
