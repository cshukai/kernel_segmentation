import cv2
import numpy as np

# build rdd and take one element for testing purpose
L = sc.binaryFiles('hdfs://localhost:9000/*.tiff').take(1)

# convert to bytearray and then to np array
file_bytes = np.asarray(bytearray(L[0][1]), dtype=np.uint8)

# use opencv to decode the np bytes array 
R = cv2.imdecode(file_bytes,1)