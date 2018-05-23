import cv2
import numpy as np

# build rdd
tiff_rdd = sc.binaryFiles('hdfs://localhost:9000/*.tiff')

# transform to array that cv can use
def tiff2CvArr(element):
      file_bytes = np.asarray(bytearray(element), dtype=np.uint8) #TypeError: unicode argument without an encoding
      R = cv2.imdecode(file_bytes,1) #1-3 channel
      return R

imgarr_rdd=tiff_rdd.map(tiff2CvArr)