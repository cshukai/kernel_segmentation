library("tiff")
library("png")

background=readTIFF("DSC_0795.NEFleft.tiff")
kernel= readTIFF("DSC_0795.NEF.tiff")


############################first deriviate: combined #############################
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
        this_idx=c(this_row_idx[j]+1,i)
        blackout_idx=rbind(blackout_idx,this_idx)
    }
}

test_img=kernel
for(i in 1:nrow(blackout_idx)){
    test_img[blackout_idx[i,1],blackout_idx[i,2],1]=0
    test_img[blackout_idx[i,1],blackout_idx[i,2],2]=0
    test_img[blackout_idx[i,1],blackout_idx[i,2],3]=0
}
writePNG(test_img,'grad_Test.png') 


############################first deriviate:  #############################


##################################secondary derivitive : combined #######################################333
b_r_2nd=diff(b_r_1st)
b_g_2nd=diff(b_g_1st)
b_b_2nd=diff(b_b_1st)
k_r_2nd=diff(k_r_1st)
k_g_2nd=diff(k_g_1st)
k_b_2nd=diff(k_b_1st)

b_2nd_total=abs(b_r_2nd)+abs(b_g_2nd)+abs(b_b_2nd)
k_2nd_total=abs(k_r_2nd)+abs(k_g_2nd)+abs(k_b_2nd)

y_cutoff=max(b_2nd_total)


blackout_idx=NULL
for(i in 1:ncol(k_2nd_total)){
    this_row_idx=which(k_2nd_total[,i]>y_cutoff)
    for(j in 1:length(this_row_idx)){
        this_idx=c(this_row_idx[j]+1,i)
        blackout_idx=rbind(blackout_idx,this_idx)
    }
}


test_img=kernel
for(i in 1:nrow(blackout_idx)){
    test_img[blackout_idx[i,1],blackout_idx[i,2],1]=0
    test_img[blackout_idx[i,1],blackout_idx[i,2],2]=0
    test_img[blackout_idx[i,1],blackout_idx[i,2],3]=0
}
writePNG(test_img,'grad_Test2.png') 
