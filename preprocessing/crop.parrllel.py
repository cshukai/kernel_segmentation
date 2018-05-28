#continue from preprocessing/input.parallel.py


def getCorrMatrix(deeperRow,rawImgArr,is4Column):
    corMax=[]
    if(is4Column):
        for i in range(deeperRow.width):
            if i<deeperRow.width-1:
                left=[]
                right=[]
                for j in range(deeperRow.height):
                    left.append(sum(rawImgArr[j,i,:]))
                    right.append(sum(rawImgArr[j,i+1,:]))
                corMax.append(pearsonr(left,right))
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