import cv2
import numpy as np
import os
import mmlspark
from mmlspark import toNDArray

IMAGE_PATH="hdfs://localhost:9000/"
images = spark.readImages(IMAGE_PATH, recursive = True, sampleRatio = 1.0).cache()
images.printSchema()
images.select('image.width').show()

'''
                                                                           
|width|
+-----+
| 3872|
| 3872|
| 3872|
| 3900|
| 3900|
| 3900|
|  206|
+-----+
'''