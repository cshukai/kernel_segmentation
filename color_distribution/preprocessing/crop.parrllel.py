#continue from preprocessing/pipeline.spark.py
import scipy.ndimage
from keras import layers
from keras import models
from skimage.util import view_as_windows

########### for small-scale test##############
x=images.first()
y=x.image
z=toNDArray(y)

#####################approach 1 for image patch########


def img2patches(ndarr,patch_width,patch_height,nchannel):
    window_shape = (patch_width, patch_height,nchannel)
    out=view_as_windows(ndarr,window_shape)
    return(out)

patches=img2patches(z,28,28,3)

#############


#############convolution to get image patches################
#but does convolution l
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation=None, input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.summary()
################## 

m=np.zeros(z.shape)
scipy.ndimage.median_filter(z,size=3,output=m)
###################################################3


def getCorrMatrix(deeperRow,rawImgArr,is4Column):
    f1=open('./cor_r_test.txt', 'w+')
    f2=open('./cor_g_test.txt', 'w+')
    f3=open('./cor_b_test.txt', 'w+')
    corMax=[]
    if(is4Column):
        for i in range(deeperRow.width):
            if i<deeperRow.width-1:
                print >>f1, 'width'+str(i)+'\n'
                print>>f1, str(pearsonr(rawImgArr[:,i,0],rawImgArr[:,i+1,0]))+'\n'
                print >>f2, 'width'+str(i)+'\n'
                print>>f2, str(pearsonr(rawImgArr[:,i,1],rawImgArr[:,i+1,1]))+'\n'
                print >>f3, 'width'+str(i)+'\n'
                print>>f3, str(pearsonr(rawImgArr[:,i,2],rawImgArr[:,i+1,2]))+'\n'
                #corMax.append(pearsonr(left,right))
    else:
        print("")    
    return corMax    
    

def ColumnCorrKmean(row):
    deeperRow=row.image
    arr=toNDArray(deeperRow)
    out=getCorrMatrix(deeperRow,arr,True)
    return(out)



def findVerticalBondary(row):
    deeperRow=row.image
    arr=toNDArray(deeperRow)       