library("tiff")
library(abind)
library("OpenImageR")
library("gpur")

left_bk=readTIFF("DSC_0785.tiffleft.tiff")
right_bk=readTIFF("DSC_0785.tiffright.tiff")
bot_bk=readTIFF("DSC_0785.tiffdown.tiff")
im= readTIFF("DSC_0785.tiffkernel.tiff")
raw=readTIFF("DSC_0785.tiff")


########################actually Feri-Chen's algorithm seems to work well#####################3
meths=c('Sobel', 'Prewitt', 'Roberts_cross', 'Frei_chen', 'Scharr', 'LoG')
convs=c('same','full')
for(i in 1:length(meths)){
    for(j in 1: length(convs)) {
        prefix=paste(meths[i],convs[j],sep="_")
        outname=paste(prefix,"tiff",sep=".")
        out=edge_detection(raw, method = meths[i], conv_mode = convs[j]) 
        writeTIFF(out,outname)
    }
}


###############see how segmentation correlate with blue-channel based cut-off###########3
bk_pixel=c(as.vector(left_bk[,,3]),as.vector(right_bk[,,3]),as.vector(bot_bk[,,3]))
cutoff=min(bk_pixel)

while(cutoff<max(bk_pixel)){
bm = im[,,3] < cutoff
imb <- im[,,3] * bm
imr <- im[,,1] * bm
img <- im[,,2] * bm
out <- abind(imr,img,imb,along=3)
prefix=paste("seg",as.character(cutoff),sep="_")
filename=paste(prefix,"tiff",sep=".")
writeTIFF(out,filename)    
cutoff=cutoff+0.1
}


cutoff=0.51

bm = im[,,3] < cutoff
imb <- im[,,3] * bm
imr <- im[,,1] * bm
img <- im[,,2] * bm
out <- abind(imr,img,imb,along=3)
prefix=paste("seg",as.character(cutoff),sep="_")
filename=paste(prefix,"tiff",sep=".")
writeTIFF(out,filename) 

#################optimization
seg_1=readTIFF("seg_0.466666666666667.tiff")
seg_1_o= edge_detection(seg_1, method = 'Frei_chen', conv_mode = 'same')