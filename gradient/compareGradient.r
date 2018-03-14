library("tiff")
library("png")

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
y_cutoff=max(b_1st_total)

k_r_1st=NULL
k_g_1st=NULL
k_b_1st=NULL
for(i in 1:ncol(kernel)){
    k_r_1st=cbind(k_r_1st,diff(kernel[,i,1]))
    k_g_1st=cbind(k_g_1st,diff(kernel[,i,2]))
    k_b_1st=cbind(k_b_1st,diff(kernel[,i,3]))
}


k_1st_total=abs(k_r_1st)+abs(k_g_1st)+abs(k_b_1st)

blackout_idx=NULL
for(i in 1:ncol(k_1st_total)){
    this_row_idx=which(k_1st_total[,i]>y_cutoff)
    for(j in 1:length(this_row_idx)){
        this_idx=c(this_row_idx[j],i)
        blackout_idx=rbind(blackout_idx,this_idx)
    }
}

test_img=kernel
for(i in 1:nrow(blackout_idx)){
    test_img[blackout_idx[i,1],blackout_idx[i,2],1]=0
    test_img[blackout_idx[i,1],blackout_idx[i,2],2]=0
    test_img[blackout_idx[i,1],blackout_idx[i,2],3]=0
}
write(test_img,file='grad_Test.png') 