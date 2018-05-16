import cv2
import numpy as np
import os



def rdd2RgbMatrix(img):
    file_bytes = np.asarray(bytearray(img[0][1]), dtype=np.uint8)
    R = cv2.imdecode(file_bytes,1)
    return(R)

# example: https://stackoverflow.com/questions/28731140/using-pyspark-read-write-2d-images-on-hadoop-file-system
# this uses take which return a list but first function will return tuple , I guess that is why the runtime error
# was there
imageRdds = sc.binaryFiles('hdfs://localhost:9000/*.tiff')
rgbMs=imageRdds.map(rdd2RgbMatrix)
