#continue from preprocessing/input.parallel.py
from scipy.stats.stats import pearsonr
from mmlspark import toNDArray
from sklearn.cluster import KMeans
import sklearn.metrics as metrics
import cProfile

def getCorrMatrix(deeperRow,rawImgArr,is4Column):
    corMax=[]
    if(is4Column):
        for i in range(deeperRow.width):
            if i<deeperRow.width:
                left=[]
                right=[]
                for j in range(deeperRow.height):
                    left.append(sum(rawImgArr[i,j,:]))
                    right.append(sum(rawImgArr[i+1,j,:]))
                    corMax.append(pearsonr(left,right))
    else:
        print("")    
    return corMax    
    

def ColumnCorrKmean(row):
    deeperRow=row.image
    arr=toNDArray(deeperRow)
    out=getCorrMatrix(deeperRow,arr,True)
    return(out)


cProfile.run("x=images.foreach(ColumnCorrKmean)")

def findBondary(row):
    deeperRow=row.image
    arr=toNDArray(deeperRow)       