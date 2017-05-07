# -*- coding:UTF-8-*-
'''
Created on 2017年5月5日

@author: xsh
'''
import tensorflow as tf

import Input_Data

class parameters():
    def __init__(self):
        print()

    def init_parameters(self,learning_rate=0.001,
                              training_iters=20000,
                              batch_size=128,
                              display_step=10,
                              
                              n_input=784,n_classes=10,dropout = 0.75):

        self.init_train_parameters(learning_rate,
                              training_iters,
                              batch_size,
                              display_step)
        
        self.init_network_parameters(n_input,n_classes,dropout)
        
    def init_train_parameters(self,
                              learning_rate = 0.001,
                              training_iters = 20000,
                              batch_size = 128,
                              display_step = 10):
        """
                    初始化训练参数
        Args:
            learning_rate: float, 学习速率
            training_iters: int, 训练迭代次数
            batch_size: int, 每次数据读入量
            display_step: int 多少步长显示一次结果
        
        return:
            None
        """
        self.learning_rate = learning_rate
        self.training_iters = training_iters
        self.batch_size = batch_size
        self.display_step = display_step
        
    def init_network_parameters(self,n_input,n_classes,dropout = 0.75):
        """
                    初始化神经网络的输入参数
        Args:
            n_input: int, 每条数据的维数
            n_classes: int ,数据的总类别
            dropout: float, 防止过度拟合  probability to keep units
        
        return
            None
        """
        # Network Parameters
        self.n_input = n_input # MNIST data input (img shape: 28*28)
        self.n_classes = n_classes # MNIST total classes (0-9 digits)
        self.dropout = dropout # Dropout, probability to keep units
        
#     def init
    

parameters = parameters()
parameters.init_parameters(learning_rate = 0.001,
                              training_iters = 20000,
                              batch_size = 128,
                              display_step=10,                              
                              n_input=784,n_classes=10,dropout = 0.75)
# tf Graph input
x = tf.placeholder(tf.float32, [None, parameters.n_input])
y = tf.placeholder(tf.float32, [None, parameters.n_classes])

keep_prob = tf.placeholder(tf.float32) #dropout (keep probability)


# Create some wrappers for simplicity
def conv2d(x, W, b, strides=1,padding='SAME'):
    # Conv2D wrapper, with bias and relu activation
    # padding='SAME' "VALID"
    x = tf.nn.conv2d(x, W, strides=[1, strides, strides, 1], padding='SAME')
    x = tf.nn.bias_add(x, b)
    return tf.nn.relu(x)


def maxpool2d(x, k=2):
    # MaxPool2D wrapper
    return tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, k, k, 1],
                          padding='VALID')


# Create model
def conv_net(x, weights, biases, dropout):
    # Reshape input picture
    print(x.get_shape())
    
    x = tf.reshape(x, shape=[-1, 28, 28, 1])
    
    print(x.get_shape())
#     exit(0)
    # Convolution Layer
    conv1 = conv2d(x, weights['wc1'], biases['bc1'])
    # Max Pooling (down-sampling)
    conv1 = maxpool2d(conv1, k=5)

    print(conv1.get_shape())
    exit()

    # Convolution Layer
    conv2 = conv2d(conv1, weights['wc2'], biases['bc2'])
    # Max Pooling (down-sampling)
    conv2 = maxpool2d(conv2, k=2)

    # Fully connected layer
    # Reshape conv2 output to fit fully connected layer input
    fc1 = tf.reshape(conv2, [-1, weights['wd1'].get_shape().as_list()[0]])
    fc1 = tf.add(tf.matmul(fc1, weights['wd1']), biases['bd1'])
    fc1 = tf.nn.relu(fc1)
    # Apply Dropout
    fc1 = tf.nn.dropout(fc1, dropout)

    # Output, class prediction
    out = tf.add(tf.matmul(fc1, weights['out']), biases['out'])
    return out

# Store layers weight & bias
weights = {
    # 5x5 conv, 1 input, 32 outputs
    'wc1': tf.Variable(tf.random_normal([5, 5, 1, 32])),
    # 5x5 conv, 32 inputs, 64 outputs
    'wc2': tf.Variable(tf.random_normal([5, 5, 32, 64])),
    # fully connected, 7*7*64 inputs, 1024 outputs
    'wd1': tf.Variable(tf.random_normal([7*7*64, 1024])),
    # 1024 inputs, 10 outputs (class prediction)
    'out': tf.Variable(tf.random_normal([1024, parameters.n_classes]))
}

biases = {
    'bc1': tf.Variable(tf.random_normal([32])),
    'bc2': tf.Variable(tf.random_normal([64])),
    'bd1': tf.Variable(tf.random_normal([1024])),
    'out': tf.Variable(tf.random_normal([parameters.n_classes]))
}

# Construct model
pred = conv_net(x, weights, biases, keep_prob)

# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=parameters.learning_rate).minimize(cost)

# Evaluate model
correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initializing the variables
init = tf.global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)
    step = 1
    # Keep training until reach max iterations
    while step * parameters.batch_size < parameters.training_iters:
        batch_x, batch_y = mnist.train.next_batch(parameters.batch_size)
        # Run optimization op (backprop)
        sess.run(optimizer, feed_dict={x: batch_x, y: batch_y,
                                       keep_prob: 0.3})
        if step % parameters.display_step == 0:
            # Calculate batch loss and accuracy
            loss, acc = sess.run([cost, accuracy], feed_dict={x: batch_x,
                                                              y: batch_y,
                                                              keep_prob: 1.})
            print("Iter " + str(step*parameters.batch_size) + ", Minibatch Loss= " + \
                  "{:.6f}".format(loss) + ", Training Accuracy= " + \
                  "{:.5f}".format(acc))
        step += 1
    print("Optimization Finished!")

    # Calculate accuracy for 256 mnist test images
    print("Testing Accuracy:", \
        sess.run(accuracy, feed_dict={x: mnist.test.images[:256],
                                      y: mnist.test.labels[:256],
                                      keep_prob: 1.}))
    