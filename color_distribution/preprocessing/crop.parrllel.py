#continue from preprocessing/pipeline.spark.py
import scipy.ndimage
from skimage.util import view_as_windows
from sklearn.cluster import KMeans
from PIL import Image
from scipy.stats import ks_2samp
from sklearn import decomposition
import random
from collections import Counter
import pandas as pd

########### for small-scale test##############
x=images.first()
y=x.image
z=toNDArray(y)
############################################


def img2patches(ndarr,patch_width,patch_height,nchannel,stride):
    window_shape = (patch_width, patch_height,nchannel)
    out=view_as_windows(ndarr,window_shape,step=stride)
    return(out)


#shape=(n_samples, n_features) to fit the input format of kmean
def reformPatches4Clustering(patches,pooling):  
    n_samples=patches.shape[0]*patches.shape[1]
    n_features=patches.shape[5]# channel num
    if(pooling==0):
        n_features=n_features*4
        out=np.zeros(shape=( n_samples,n_features),dtype=int) #[R_G_B][toplef,topright,bottomleft,bottomright]
        counter=0
        for i in range(patches.shape[1]):
            for j in range(patches.shape[0]):
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
                #print(counter)
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
unique, counts = np.unique(kmean.labels_, return_counts=True)
dict(zip(unique, counts))



######################## testing if clusters are different from each other########3
a=kmean.labels_

potential_bg_gr=patch_tbl[np.where(a==0),:]
potential_fg_gr=patch_tbl[np.where(a==1),:]

df_bg=pd.DataFrame(potential_bg_gr[0,:,:])
df_fg=pd.DataFrame(potential_fg_gr[0,:,:])

df_bg.to_csv('~/bfg.csv')
df_fg.to_csv('~/pfg.csv')

def testRGB(patch_tbl,gr1,gr2,reduction,test):
    if()
    





################visualization for manual validation#####################3
a=kmean.labels_
def vizIdvPatches4KmeanResult(kmeanLabels,patches,patch_tbl):
    for i in range(patch_tbl.shape[0]):
        out[0,0,0]=patch_tbl[i,0]
        out[0,0,1]=patch_tbl[i,1]
        out[0,0,2]=patch_tbl[i,2]
        out[0,1,0]=patch_tbl[i,3]
        out[0,1,1]=patch_tbl[i,4]
        out[0,1,2]=patch_tbl[i,5]
        out[1,0,0]=patch_tbl[i,6]
        out[1,0,1]=patch_tbl[i,7]
        out[1,0,2]=patch_tbl[i,8]
        out[1,1,0]=patch_tbl[i,9]
        out[1,1,1]=patch_tbl[i,10]
        out[1,1,2]=patch_tbl[i,11]
        outname=str(i)+"_"+str(kmeanLabels[i])+".png"
        img = Image.fromarray(out, 'RGB')
        img.save(outname)


'''
this work but need to fit the screen dimension, not the error of code itself
vizIdvPatches4KmeanResult(a,patches,patch_tbl)

def vizAssemblePatchSquare4KmeanResult(a,patches,patch_tbl):
    potential_bg_gr=patch_tbl[np.where(a==0),:]
    potential_fg_gr=patch_tbl[np.where(a==1),:]
    
    
    bg_out=np.zeros(shape=(2,2,3),dtype=int)
    bg_out[0,0,0]=potential_bg_gr[0,0,0]
    bg_out[0,0,1]=potential_bg_gr[0,0,1]
    bg_out[0,0,2]=potential_bg_gr[0,0,2]
    bg_out[0,1,0]=potential_bg_gr[0,0,3]
    bg_out[0,1,1]=potential_bg_gr[0,0,4]
    bg_out[0,1,2]=potential_bg_gr[0,0,5]
    bg_out[1,0,0]=potential_bg_gr[0,0,6]
    bg_out[1,0,1]=potential_bg_gr[0,0,7]
    bg_out[1,0,2]=potential_bg_gr[0,0,8]
    bg_out[1,1,0]=potential_bg_gr[0,0,9]
    bg_out[1,1,1]=potential_bg_gr[0,0,10]
    bg_out[1,1,2]=potential_bg_gr[0,0,11]
    
    for i in range(1,potential_bg_gr.shape[1]):
        out=np.zeros(shape=(2,2,3),dtype=int)
        out[0,0,0]=potential_bg_gr[0,i,0]
        out[0,0,1]=potential_bg_gr[0,i,1]
        out[0,0,2]=potential_bg_gr[0,i,2]
        out[0,1,0]=potential_bg_gr[0,i,3]
        out[0,1,1]=potential_bg_gr[0,i,4]
        out[0,1,2]=potential_bg_gr[0,i,5]
        out[1,0,0]=potential_bg_gr[0,i,6]
        out[1,0,1]=potential_bg_gr[0,i,7]
        out[1,0,2]=potential_bg_gr[0,i,8]
        out[1,1,0]=potential_bg_gr[0,i,9]
        out[1,1,1]=potential_bg_gr[0,i,10]
        out[1,1,2]=potential_bg_gr[0,i,11]
        bg_out=np.vstack((bg_out,out))
        img = Image.fromarray(bg_out, 'RGB')
        img.save("test.bg.png")
########################################################
       
'''
>>> this_patch=np.array([[[out[i,0],out[i,3]],[out[i,6],out[i,9]]],[[out[i,1],out[i,4]],[out[i,7],out[i,10]]],[[out[i,2],out[i,5]],[out[i,8],out[i,11]]]])        
>>> this_patch.shape
(3, 2, 2)
''''
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