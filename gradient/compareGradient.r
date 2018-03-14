library("tiff")
library("imager")
library(pracma)

background=readTIFF("DSC_0795.NEFleft.tiff")
kernel= readTIFF("DSC_0795.NEF.tiff")

b_r_1st=NULL
b_g_1st=NULL
b_b_1st=NULL
for(i in 1:ncol(background)){
    b_r_1st=cbind(b_r_1st,diff(background[,i,1]))
    b_g_1st=cbind(b_g_1st,diff(background[,i,2]))
    b_b_1st=cbind(b_b_1st,diff(background[,i,3]))
}

b_1st_total=abs(b_r_1st)+abs(b_g_1st)+abs(b_b_1st)
x_cutoff=max(b_1st_total)

k_r_1st=NULL
k_g_1st=NULL
k_b_1st=NULL
for(i in 1:ncol(kernel)){
    k_r_1st=cbind(k_r_1st,diff(kernel[,i,1]))
    k_g_1st=cbind(k_g_1st,diff(kernel[,i,2]))
    k_b_1st=cbind(k_b_1st,diff(kernel[,i,3]))
}


k_1st_total=abs(k_r_1st)+abs(k_g_1st)+abs(k_b_1st)


kernel.r=as.cimg(kernel)
gr=imgradient(as.cimg(kernel),"xy")
png('gr.png')
plot(gr,layout="row")
dev.off()