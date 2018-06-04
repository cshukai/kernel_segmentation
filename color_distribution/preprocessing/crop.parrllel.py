#continue from preprocessing/pipeline.spark.py
import scipy.ndimage
x=images.first()
y=x.image
z=toNDArray(y)
m=numpy.zeros(z.shape)
m=scipy.ndimage.median_filter(z,size=3)
# filter is not allowed to pass the edge of image in this function
def squareFilterScan(ndarr,orientation,fiterSize,stride): #orientation 1-columnwise,2-row-wise
     


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