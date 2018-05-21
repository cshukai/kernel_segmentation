#pyspark --num-executors 2 --driver-memory 5g --executor-memory 5g --packages Azure:mmlspark:0.12
import cv2
import numpy as np
import os
import pyspark

spark = pyspark.sql.SparkSession.builder.appName("MyApp") \
            .config("spark.jars.packages", "Azure:mmlspark:0.12") \
            .getOrCreate()

import mmlspark
from mmlspark import toNDArray
from mmlspark import ImageTransformer
from mmlspark import ImageWriter
from PIL import Image


IMAGE_PATH="hdfs://localhost:9000/"
images = spark.readImages(IMAGE_PATH, recursive = True, sampleRatio = 1.0)
#images.printSchema()
#images.select('image.width').show()

tr_rgb2lab = (ImageTransformer()                  # images are resized and then cropped
      .setOutputCol("transformed")
      .colorFormat(cv2.COLOR_RGB2Lab)
      )

im_lab = tr_rgb2lab.transform(images).select("transformed")
ImageWriter.write(im_lab)