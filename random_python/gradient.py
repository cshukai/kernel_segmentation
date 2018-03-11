from PIL import Image
import numpy
from scipy.stats.stats import pearsonr

im = Image.open("DSC_0795.NEF") 

pix = im.load()

width=im.size[0]
height=im.size[1]

##################find where pure background sections are , assuming the kernels are located in the middle##############################
cor_result_vertical=[] # side
for i in range(width):
    if i<width-1:
        left=[]
        right=[]
        for j in range(height):
            left.append(sum(pix[i,j]))
            right.append(sum(pix[i+1,j]))
        
        cor_result_vertical.append(pearsonr(left,right))


cor_result_horizontal=[] # top and botton
middle=height/2
for i in range(height):
    if i<height-1:
        top=numpy.array([])
        bot=numpy.array([])
        for j in range(width):
            top=numpy.append(top,sum(pix[j,i]))
            bot=numpy.append(bot,sum(pix[j,i+1]))
            if numpy.sum(top)==0:
                top=numpy.add(top,1)
            if numpy.sum(bot)==0:
                bot=numpy.add(bot,1)    
                
            
        cor_result_horizontal.append(pearsonr(top,bot))


cutoff_vertical=0.99   
for i in range(len(cor_result_vertical)):
    this_cor=cor_result_vertical[i][0]
    if this_cor<=cutoff_vertical:
        left=i+1
        break

for i in range(len(cor_result_vertical)-1,-1,-1):
    this_cor=cor_result_vertical[i][0]
    if this_cor<=cutoff_vertical:
        right=i+1
        break    

cutoff_horizontal=0.9
for i in range(pearsonr):
    if i<len(cor_result)-1:

top = 1
right = 138
bottom = height
cropped_example = im.crop((left, top, right, bottom))



        
# find the median  RGB values  of background area

        