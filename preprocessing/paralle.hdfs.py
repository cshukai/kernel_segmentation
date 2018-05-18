import cv2
import numpy as np
import os
import mmlspark
from mmlspark import toNDArray
from mmlspark import ImageTransformer


IMAGE_PATH="hdfs://localhost:9000/"
images = spark.readImages(IMAGE_PATH, recursive = True, sampleRatio = 1.0).cache()
#images.printSchema()
#images.select('image.width').show()

tr = (ImageTransformer()                  # images are resized and then cropped
      .setOutputCol("transformed")
      .resize(height = 200, width = 200)
      .crop(0, 0, height = 180, width = 180) )

small = tr.transform(images).select("transformed")
