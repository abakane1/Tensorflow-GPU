import tensorflow as tf
import numpy as np
A = tf.placeholder(tf.float64, shape=(None, 3))
B = A + 5

with tf.Session() as sess:
    B_val_1 = B.eval(feed_dict={A: [[1,2,3]]})

print (B_val_1)