from PIL import Image
import numpy
from scipy.stats.stats import pearsonr

im = Image.open("DSC_0795.NEF") 

pix = im.load()

width=im.size[0]
height=im.size[1]

##################find where pure background sections are , assuming the kernels are located in the middle and color checker is on the top or bottom##############################
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
        left=i
        break

for i in range(len(cor_result_vertical)-1,-1,-1):
    this_cor=cor_result_vertical[i][0]
    if this_cor<=cutoff_vertical:
        right=i+2
        break    

cutoff_horizontal=0.9
for i in range((len(cor_result_horizontal)/2)-1,-1,-1):
    this_cor=cor_result_horizontal[i][0]
    if this_cor>=cutoff_horizontal:
        top=i+1
        break

for i in range((len(cor_result_horizontal)/2)-1,len(cor_result_horizontal)):
    this_cor=cor_result_horizontal[i][0]
    if this_cor>=cutoff_horizontal:
        bot=i+1
        break


cropped_example = im.crop((left, top, right, bot))# extract kernel
out_png=im.filename+'.png'
out_tiff=im.filename+'.tiff'
cropped_example.save(out_png)
cropped_example.save(out_tiff)

# extract left  background regions
left2=left-1
cropped_left=im.crop((1,top,left2,bot))        
left_png=im.filename+'left.png'
left_tiff=im.filename+'left.tiff' 
cropped_left.save(left_png)
cropped_left.save(left_tiff)
