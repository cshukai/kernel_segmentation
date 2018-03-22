from PIL import Image
import numpy
from scipy.stats.stats import pearsonr

im = Image.open("DSC_0785.NEF") 
im2 = Image.open("DSC_0785.tiff") 

pix = im.load()
pix2 = im2.load()

width=im.size[0]
height=im.size[1]

width2=im2.size[0]
height2=im2.size[1]

width_ratio=width2/width
height_ratio=numpy.round((height2/height)*0.9)
height_ratio=height2/height

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
            #print(top)
            #print(bot)
            #print('----')
            if numpy.sum(top)==0:
                top=numpy.add(top,1) 
            if numpy.sum(bot)==0:
                bot=numpy.add(bot,1)    
                
            
        cor_result_horizontal.append(pearsonr(top,bot))

left=None
cutoff_vertical=0.99
for i in range(len(cor_result_vertical)):
    this_cor=cor_result_vertical[i][0]
    #print(this_cor)
    if this_cor<=cutoff_vertical:
        print('here')
        left=i
        break
    
right=None
for i in range(len(cor_result_vertical)-1,-1,-1):
    this_cor=cor_result_vertical[i][0]
    if this_cor<=cutoff_vertical:
        right=i+2
        break    

top=None
cutoff_horizontal=0.99
for i in range((len(cor_result_horizontal)/2)-1,-1,-1):
    this_cor=cor_result_horizontal[i][0]
    if this_cor>=cutoff_horizontal:
        top=i+1
        break

bot=None
for i in range((len(cor_result_horizontal)/2)-1,len(cor_result_horizontal)):
    this_cor=cor_result_horizontal[i][0]
    if this_cor>=cutoff_horizontal:
        bot=i+1
        break

left=left*width_ratio
right=right*width_ratio
top=top*height_ratio
bot=bot*height_ratio

im=im2

cropped_example = im.crop((left, top, right, bot))# extract kernel
out_png=im.filename+'.kernel.png'
out_tiff=im.filename+'kernel.tiff'
cropped_example.save(out_png)
cropped_example.save(out_tiff)

# extract left  background regions
left2=left-1
cropped_left=im.crop((1,top,left2,bot))        
left_png=im.filename+'left.png'
left_tiff=im.filename+'left.tiff' 
cropped_left.save(left_png)
cropped_left.save(left_tiff)

#extract right background regions
left3=right+1
cropped_right=im.crop((left3,top,width,bot))
right_png=im.filename+'right.png'
right_tiff=im.filename+'right.tiff' 
cropped_right.save(right_png)
cropped_right.save(right_tiff)


#extract down background regions
top2=bot+1
bot2=0
middle=width/2
for i in (range(height,-1,-1)):
    print(i)
    this_sum=numpy.sum(pix[middle,i-1])
    if(this_sum)>0:
        bot2=i-2
        break
cropped_down=im.crop((0,top2,width,bot2))
down_png=im.filename+'down.png'
down_tiff=im.filename+'down.tiff' 
cropped_down.save(down_png)
cropped_down.save(down_tiff)