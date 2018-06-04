#load b channel 
d=read.csv("test_lab_matrix.csv")

left=d[,1:219]
right=d[,3423:ncol(d)]
bottom=d[2444:nrow(d),]
backround=NULL
for(i in 1:nrow(right)){
    background=c(background,right[i,])
}
for(i in 1:nrow(left)){
    background=c(background,left[i,])
}
for(i in 1:nrow(bottom)){
    background=c(background,bottom[i,])
}


background2=unlist(background)
png("background_lab.png")
#hist(background2,main="Background in Lab Space",xlim=c(-100,100))
hist(background2,main="Background in Lab Space",xlab="Pixel Values")

dev.off()



non_background=d[1:2443,22:3422]

nonbackground=NULL
for(i in 1:nrow(non_background)){
    nonbackground=c(nonbackground,non_background[i,])
}

nonbackground2=unlist(nonbackground)
png("nonbackground_lab.png")
#hist(nonbackground2,main="Non-Background in Lab Space",xlim=c(-100,100))
hist(nonbackground2,main="Non-Background in Lab Space",xlab="Pixel Values")

dev.off()


save.image("lab.RData") 