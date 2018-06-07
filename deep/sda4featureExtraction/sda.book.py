#Hands-On Machine Learning with Scikit-Learn and TensorFlow ch15

import tensorflow as tf

noise_level = 1.0
X = tf.placeholder(tf.float32, shape=[None, n_inputs])
X_noisy = X + noise_level * tf.random_normal(tf.shape(X))

hidden1 = tf.layers.dense(X_noisy, n_hidden1, activation=tf.nn.relu,name="hidden1")