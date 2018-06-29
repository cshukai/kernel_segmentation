# pyspark --num-executors 6 --driver-memory 6g --executor-memory 1g --packages Azure:mmlspark:0.12
# this is the entry point of the pipeline
import cv2
import numpy as np
import os
import mmlspark 
from mmlspark import toNDArray
from mmlspark import ImageTransformer
from mmlspark import ImageWriter
from PIL import Image
from pyspark.ml.linalg import Vectors
from scipy.stats.stats import pearsonr
from mmlspark import toNDArray
from sklearn.cluster import KMeans
import sklearn.metrics as metrics
import cProfile


#IMAGE_PATH="hdfs://localhost:9000/"
IMAGE_PATH=os.getcwd()+'/DSC_0785.tiff'
images = spark.readImages(IMAGE_PATH, recursive = True, sampleRatio = 1.0)

x=images.foreach(ColumnCorrKmean) # code may work but output not retrievalbe from worker node

testcluster=KMeans(ncluster=3)
testcluster.fit(x) # does x has to be panda dataframe ?

def rawDf2ColumnWiseDf(row):
    deeperRow=row.image
    arr=toNDArray(deeperRow)
    r_rdd=spark.sparkContext.parallelize(arr[:,:,0])
    g_rdd=spark.sparkContext.parallelize(arr[:,:,1])
    b_rdd=spark.sparkContext.parallelize(arr[:,:,2])
    #not sure if a list should be used here to store three separate rdd as it seems to put huge pressure on headnode
    

tr_rgb2lab = (ImageTransformer() 
      .setOutputCol("transformed")
      .colorFormat(cv2.COLOR_BGR2GRAY) # accroding to "machine learing and opencv" , you should use BGR when converting RGB to HSV, I suppose the same for rgb to lab
      #.colorFormat(cv2.COLOR_BGR2Lab)
      #.colorFormat(cv2.COLOR_RGB2Lab) 
      )

im_lab = tr_rgb2lab.transform(images).select("transformed")


def showType(row):
      print type(row)

def saveImagesFromDataFrame(row):
      deeperRow=row.transformed
      inputnames=str(deeperRow.path).split("/") # doesn't seem like it is row object since it can't access path directly
      outname=inputnames[len(inputnames)-1]+".cvt.tiff"
      arr=toNDArray(deeperRow)
      cv2.imwrite(outname,arr)
      
      
im_lab.foreach(saveImagesFromDataFrame)
im_lab.foreach(showType)  # pyspark.sql.types.Row

#>>> x=im_lab.first()
# >>> x.__fields__
# ['transformed']
# >>> y=x.transformed
# >>> type(y)
# <class 'pyspark.sql.types.Row'>
# >>> y.__fields__
# ['path', 'height', 'width', 'type', 'bytes']