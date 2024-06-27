import tensorflow as tf

# Create a constant tensor
a = tf.constant(5.0)
b = tf.constant(6.0)

# Add the two tensors
c = tf.add(a, b)

with tf.Session() as sess:
    print(sess.run(c))