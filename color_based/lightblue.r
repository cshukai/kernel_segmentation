library("tiff")
library("png")
library(abind)

left_bk=readTIFF("DSC_0785.tiffleft.tiff")
right_bk=readTIFF("DSC_0785.tiffright.tiff")
bot_bk=readTIFF("DSC_0785.tiffdown.tiff")
im= readTIFF("DSC_0785.tiffkernel.tiff")

bk_pixel=c(as.vector(left_bk[,,3]),as.vector(right_bk[,,3]),as.vector(bot_bk[,,3]))
cutoff=min(bk_pixel)

bm = im[,,3] < cutoff


imb <- im[,,3] * bm
imr <- im[,,1] * bm
img <- im[,,2] * bm
out <- abind(imr,img,imb,along=3)

writeTIFF(out,"seg.tiff")