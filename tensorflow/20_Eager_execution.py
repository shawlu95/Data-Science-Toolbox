import tensorflow as tf

# tf.enable_eager_execution() # deprecated
tf.compat.v1.enable_eager_execution()

# ___
# To compute multiple gradients over the same computation,
# create a persistent gradient tape.
x = tf.ones((2, 2))
with tf.GradientTape(persistent=True) as t:
  t.watch(x)
  y = tf.reduce_sum(x)
  z = tf.multiply(y, y)
print(z.numpy())

# ___
# Derivative of z with respect to the original input tensor x
dz_dx = t.gradient(z, x)
for i in [0, 1]:
  for j in [0, 1]:
    assert dz_dx[i][j].numpy() == 8.0
# take intermediate gradient
dz_dy = t.gradient(z, y)
print(dz_dx.numpy())
print(dz_dy.numpy())

# ___
# nested gradient
x = tf.Variable(1.0)  # Create a Tensorflow variable initialized to 1.0
with tf.GradientTape() as t:
  with tf.GradientTape() as t2:
    y = x * x * x
  # Compute the gradient inside the 't' context manager
  # which means the gradient computation is differentiable as well.
  dy_dx = t2.gradient(y, x)
d2y_dx2 = t.gradient(dy_dx, x)
assert dy_dx.numpy() == 3.0
assert d2y_dx2.numpy() == 6.0
print(dy_dx.numpy())
print(d2y_dx2.numpy())
