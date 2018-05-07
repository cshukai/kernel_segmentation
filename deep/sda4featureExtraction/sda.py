# https://blog.keras.io/building-autoencoders-in-keras.html
# run this first :tensorboard --logdir=/tmp/autoencoder
import numpy as np
from keras import regularizers
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras import backend as K
from keras.callbacks import TensorBoard 

#io.imsave("keras.tiff", x_test[1])  