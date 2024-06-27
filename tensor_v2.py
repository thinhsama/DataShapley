import tensorflow as tf
#tf.compat.v1.disable_eager_execution()
# Create a constant tensor
a = tf.constant(5.0)
b = tf.constant(6.0)

# Add the two tensors
c = tf.add(a, b)

with tf.compat.v1.Session() as sess:
    print(sess.run(c))