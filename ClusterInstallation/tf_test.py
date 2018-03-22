#/usr/bin/env python
from __future__ import print_function
import tensorflow as tf

vers = tf.__version__
print(vers)
hello = tf.constant('Hello, TensorFlow!')
matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.],[2.]])
product = tf.matmul(matrix1, matrix2)

sess = tf.Session()
print(sess.run(hello))
print(sess.run(product))
sess.close()
