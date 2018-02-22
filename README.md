# extraction of kernel regions #
## color thresholding##

### RGB ###
1. the rgb pattern of background blue (B>60, R<30 , G<30)
2. potential issue:  some of the yellow kernel has shadow which has simialr RGB pattern to black kernel

##Histogram## 
1. to graysacle 
2. threshold twice since there are kernel darker/lighter than  blue 
