#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: tang_poems.py
    @time: 2019/12/22 0:03
"""
import os

import numpy as np
import tensorflow as tf
from datetime import datetime
from poetry.model import rnn_model
from poetry.poems import process_poems, generate_batch
from util_root_path import poetry_demo_root_path, osp

tf.app.flags.DEFINE_integer('batch_size', 64, 'batch size.')
tf.app.flags.DEFINE_float('learning_rate', 0.01, 'learning rate.')

tf.app.flags.DEFINE_integer('rnn_size', 128, 'rnn size.')
tf.app.flags.DEFINE_integer('num_layers', 4, 'num layers.')

# set this to 'main.py' relative path
tf.app.flags.DEFINE_string('checkpoints_dir', osp.join(poetry_demo_root_path, 'checkpoints/'), 'checkpoints save path.')
tf.app.flags.DEFINE_string('file_path', osp.join(poetry_demo_root_path, 'corpus', 'poetry.txt'), 'file name of poems.')

tf.app.flags.DEFINE_string('model_prefix', 'poems', 'model save prefix.')

tf.app.flags.DEFINE_integer('epochs', 100, 'train how many epochs.')

FLAGS = tf.app.flags.FLAGS

start_token = 'G'
end_token = 'E'


# 开始训练
def run_training():
    if not os.path.exists(os.path.dirname(FLAGS.checkpoints_dir)):
        os.mkdir(os.path.dirname(FLAGS.checkpoints_dir))
    if not os.path.exists(FLAGS.checkpoints_dir):
        os.mkdir(FLAGS.checkpoints_dir)

    poems_vector, word_to_int, vocabularies = process_poems(FLAGS.file_path)
    batches_inputs, batches_outputs = generate_batch(FLAGS.batch_size, poems_vector, word_to_int)

    input_data = tf.placeholder(tf.int32, [FLAGS.batch_size, None])
    output_targets = tf.placeholder(tf.int32, [FLAGS.batch_size, None])

    end_points = rnn_model(model='lstm', input_data=input_data, output_data=output_targets, vocab_size=len(
        vocabularies), rnn_size=FLAGS.rnn_size, num_layers=FLAGS.num_layers, batch_size=FLAGS.batch_size,
                           learning_rate=FLAGS.learning_rate)

    saver = tf.train.Saver(tf.global_variables())
    init_op = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
    with tf.Session() as sess:
        # sess = tf_debug.LocalCLIDebugWrapperSession(sess=sess)
        # sess.add_tensor_filter("has_inf_or_nan", tf_debug.has_inf_or_nan)
        sess.run(init_op)

        start_epoch = 0
        checkpoint = tf.train.latest_checkpoint(FLAGS.checkpoints_dir)
        if checkpoint:
            saver.restore(sess, checkpoint)
            print("[INFO] restore from the checkpoint {0}".format(checkpoint))
            start_epoch += int(checkpoint.split('-')[-1])
        print('[INFO] start training...')
        try:
            train_start = datetime.now()
            for epoch in range(start_epoch, FLAGS.epochs):
                epoch_start = datetime.now()
                n = 0
                n_chunk = len(poems_vector) // FLAGS.batch_size
                n_batch_start = datetime.now()
                for batch in range(n_chunk):
                    loss, _, _ = sess.run([
                        end_points['total_loss'],
                        end_points['last_state'],
                        end_points['train_op']
                    ], feed_dict={input_data: batches_inputs[n], output_targets: batches_outputs[n]})

                    if n % 100 == 0:
                        n_batch_end = datetime.now()
                        print('[INFO] Epoch: %d , cost time: %s , batch: %d , training loss: %.6f' % (
                            epoch, n_batch_end - n_batch_start, batch, loss))
                        n_batch_start = datetime.now()
                    n += 1
                if epoch % 1 == 0:
                    saver.save(sess, os.path.join(FLAGS.checkpoints_dir, FLAGS.model_prefix), global_step=epoch)
                epoch_end = datetime.now()
                print('[INFO] Epoch: %d , training cost time : %s' % (epoch, epoch_end - epoch_start))
            train_end = datetime.now()
            print('[INFO] Training cost time : %s' % (epoch, train_end - train_start))
        except KeyboardInterrupt:
            print('[INFO] Interrupt manually, try saving checkpoint for now...')
            saver.save(sess, os.path.join(FLAGS.checkpoints_dir, FLAGS.model_prefix), global_step=epoch)
            print('[INFO] Last epoch were saved, next time will start from epoch {}.'.format(epoch))


def to_word(predict, vocabs):
    t = np.cumsum(predict)
    s = np.sum(predict)
    sample = int(np.searchsorted(t, np.random.rand(1) * s))
    if sample > len(vocabs):
        sample = len(vocabs) - 1
    return vocabs[sample]


# 调用模型生成诗句
def gen_poem(begin_word):
    batch_size = 1
    print('[INFO] loading corpus from %s' % FLAGS.file_path)
    poems_vector, word_int_map, vocabularies = process_poems(FLAGS.file_path)

    input_data = tf.placeholder(tf.int32, [batch_size, None])

    end_points = rnn_model(model='lstm', input_data=input_data, output_data=None, vocab_size=len(
        vocabularies), rnn_size=FLAGS.rnn_size, num_layers=FLAGS.num_layers, batch_size=FLAGS.batch_size,
                           learning_rate=FLAGS.learning_rate)

    saver = tf.train.Saver(tf.global_variables())
    init_op = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
    with tf.Session() as sess:
        sess.run(init_op)

        checkpoint = tf.train.latest_checkpoint(FLAGS.checkpoints_dir)
        saver.restore(sess, checkpoint)

        x = np.array([list(map(word_int_map.get, start_token))])

        [predict, last_state] = sess.run([end_points['prediction'], end_points['last_state']],
                                         feed_dict={input_data: x})
        if begin_word:
            word = begin_word
        else:
            word = to_word(predict, vocabularies)
        poem = ''
        while word != end_token:
            poem += word
            x = np.zeros((1, 1))
            x[0, 0] = word_int_map[word]
            [predict, last_state] = sess.run([end_points['prediction'], end_points['last_state']],
                                             feed_dict={input_data: x, end_points['initial_state']: last_state})
            word = to_word(predict, vocabularies)
            # print(word)
        # word = words[np.argmax(probs_)]
        return poem


# 这里将生成的诗句，按照中文诗词的格式输出
# 同时方便接入应用
def pretty_print_poem(poem):
    poem_sentences = poem.split('。')
    for s in poem_sentences:
        if s != '' and len(s) > 10:
            print(s + '。')


def _main(is_train):
    if is_train:
        print('[INFO] train tang poem...')
        run_training()
    else:
        print('[INFO] write tang poem...')

        begin_word = input('开始作诗，请输入起始字:')
        poem2 = gen_poem(begin_word)
        pretty_print_poem(poem2)


def main(is_train):
    if isinstance(is_train, list):
        _main(is_train[0])
    else:
        _main(is_train)


if __name__ == '__main__':
    tf.app.run(argv=[False])
