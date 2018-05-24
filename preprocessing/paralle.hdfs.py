# pyspark --num-executors 6 --driver-memory 6g --executor-memory 1g --packages Azure:mmlspark:0.12
import cv2
import numpy as np
import os
import mmlspark
from mmlspark import toNDArray
from mmlspark import ImageTransformer
from mmlspark import ImageWriter
from PIL import Image


IMAGE_PATH="hdfs://localhost:9000/"
images = spark.readImages(IMAGE_PATH, recursive = True, sampleRatio = 1.0)

tr_rgb2lab = (ImageTransformer() 
      .setOutputCol("transformed")
      .colorFormat(cv2.COLOR_RGB2Lab)
      )

im_lab = tr_rgb2lab.transform(images).select("transformed")


def showType(row):
      print type(row)

def saveImagesFromDataFrame(row):
      deeperRow=row.transformed
      inputnames=str(deeperRow.path).split("/") # doesn't seem like it is row object since it can't access path directly
      outname=inputnames[len(inputnames)-1]
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