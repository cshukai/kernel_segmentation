import cv2
import numpy as np
import os

# build rdd and take one element for testing purpose
#L = sc.binaryFiles('hdfs://localhost:9000/*.tiff').take(1)
images = sc.binaryFiles('hdfs://localhost:9000/*.tiff')
# assuming this operation actually take two tiffs
# convert to bytearray and then to np array

def saveImage():
    

images.foreach(saveImage)
file_bytes = np.asarray(bytearray(L[0][1]), dtype=np.uint8)

# use opencv to decode the np bytes array 
R = cv2.imdecode(file_bytes,1)

#test 
#cv2.imwrite("test.tiff",R)
cv2.imwrite("test2.tiff",R)