#continue from preprocessing/pipeline.spark.py
import scipy.ndimage
from skimage.util import view_as_windows
from sklearn.cluster import KMeans
########### for small-scale test##############
x=images.first()
y=x.image
z=toNDArray(y)
############################################


def img2patches(ndarr,patch_width,patch_height,nchannel,stride):
    window_shape = (patch_width, patch_height,nchannel)
    out=view_as_windows(ndarr,window_shape,step=stride)
    return(out)

'''
counter number doesn't match patch number , need to fix this bug
2543445
>>> patches.shape[0]*patches.shape[1]
2546700
'''


def reformPatches4Clustering(patches,pooling): #shape=(n_samples, n_features) 
    n_samples=patches.shape[0]*patches.shape[1]
    n_features=patches.shape[5]# channel num
    if(pooling==0):
        n_features=n_features*4
        out=np.zeros(shape=( n_samples,n_features),dtype=int) #[R_G_B][toplef,topright,bottomleft,bottomright]
        counter=0
        for i in range(patches.shape[1]):
          #if i<patches.shape[1]-1:
            for j in range(patches.shape[0]):
              #if j<patches.shape[0]-1:
               # print(i)
               #print(j)
                this_patch_r_tl=patches[j,i][0][0][0][0]
                this_patch_g_tl=patches[j,i][0][0][0][1]
                this_patch_b_tl=patches[j,i][0][0][0][2]
                this_patch_r_tr=patches[j,i][0][0][1][0]
                this_patch_g_tr=patches[j,i][0][0][1][1]
                this_patch_b_tr=patches[j,i][0][0][1][2]
                this_patch_r_bl=patches[j,i][0][1][0][0]
                this_patch_g_bl=patches[j,i][0][1][0][1]
                this_patch_b_bl=patches[j,i][0][1][0][2]
                this_patch_r_br=patches[j,i][0][1][1][0]
                this_patch_g_br=patches[j,i][0][1][1][1]
                this_patch_b_br=patches[j,i][0][1][1][2]
                out[counter,0]=this_patch_r_tl
                out[counter,1]=this_patch_g_tl
                out[counter,2]=this_patch_b_tl
                out[counter,3]=this_patch_r_tr
                out[counter,4]=this_patch_g_tr
                out[counter,5]=this_patch_b_tr
                out[counter,6]=this_patch_r_bl
                out[counter,7]=this_patch_g_bl
                out[counter,8]=this_patch_b_bl
                out[counter,9]=this_patch_r_br
                out[counter,10]=this_patch_g_br
                out[counter,11]=this_patch_b_br
                counter=counter+1
                print(counter)
    return(out)

'''
>>> patches[0,0]
array([[[[134, 165, 222],
         [129, 167, 221]],

        [[133, 166, 222],
         [128, 169, 221]]]], dtype=uint8)
>>> patches[0,1]
array([[[[126, 169, 218],
         [119, 171, 215]],

        [[124, 169, 222],
         [117, 170, 223]]]], dtype=uint8)
>>> z[0,0]
array([134, 165, 222], dtype=uint8)
>>> z[0,1]                                                                                   
array([129, 167, 221], dtype=uint8)
>>> z[1,1]                                                                                    
array([128, 169, 221], dtype=uint8)
>>> z[1,0]                                                                                   
array([133, 166, 222], dtype=uint8)
'''


patches=img2patches(z,2,2,3,2)
patch_tbl=reformPatches4Clustering(patches,0)
#np.equal(z[0:2,0:2,:],patches[0,0,0,:,:,:]) # validation

kmean = KMeans(n_clusters=2)
cluster_result=kmean.fit(patch_tbl)
kmean.labels_ #see clustering result

''' testing
patches=img2patches(z,28,28,3)
np.equal(z[0:28,0:28,:],patches[0,0,0,:,:,:])                                             
array([[[ True,  True,  True],
        [ True,  True,  True],
        [ True,  True,  True],
        ...,
        [ True,  True,  True],
        [ True,  True,  True],
        [ True,  True,  True]],

       [[ True,  True,  True],
        [ True,  True,  True],
        [ True,  True,  True],
        ...,
        [ True,  True,  True],
        [ True,  True,  True],
        [ True,  True,  True]],

       [[ True,  True,  True],
        [ True,  True,  True],
        [ True,  True,  True],
        ...,
        [ True,  True,  True],
        [ True,  True,  True],
        [ True,  True,  True]],

       ...,

       [[ True,  True,  True],
        [ True,  True,  True],
        [ True,  True,  True],
        ...,
        [ True,  True,  True],
        [ True,  True,  True],
        [ True,  True,  True]],

       [[ True,  True,  True],
        [ True,  True,  True],
        [ True,  True,  True],
        ...,
        [ True,  True,  True],
        [ True,  True,  True],
        [ True,  True,  True]],

       [[ True,  True,  True],
        [ True,  True,  True],
        [ True,  True,  True],
        ...,
        [ True,  True,  True],
        [ True,  True,  True],
        [ True,  True,  True]]])
>>> 
'''

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