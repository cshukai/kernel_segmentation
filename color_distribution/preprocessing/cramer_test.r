library(cramer)

d_b=read.csv("bfg.csv",header=T)
d_f=read.csv("pfg.csv",header=T)

#cramer.test(as.matrix(d_b[,2:ncol(d_b)]),as.matrix(d_f[,2:ncol(d_f)]),sim="eigenvalue")
cramer.test(as.matrix(d_b[1:1000,2:ncol(d_b)]),as.matrix(d_f[1:1000,2:ncol(d_f)]),sim="eigenvalue")


# > cramer.test(as.matrix(d_b[1:1000,2:ncol(d_b)]),as.matrix(d_f[1:1000,2:ncol(d_f)]),sim="eigenvalue")

#  12 -dimensional  nonparametric Cramer-Test with kernel phiCramer 
# (on equality of two distributions) 

#         x-sample:  1000  values        y-sample:  1000  values

# critical value for confidence level  95 % :  246.0161 
# observed statistic  88331.06 , so that
#          hypothesis ("x is distributed as y") is  REJECTED .
# estimated p-value =  0.00257995 

#         [result based on eigenvalue decomposition and inverse fft]



# todo :try resample permutation approach