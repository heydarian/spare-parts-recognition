# -*- coding: utf-8 -*-
import os
from time import time
import numpy as np

import tensorflow as tf
import tensorflow.keras as k

import settings


def get_cnn_model(backbone='Inception', plot=False):
    if backbone == 'Densenet':
        base_model = k.applications.DenseNet121(include_top=False, weights='imagenet')
    elif backbone == 'Efficientnet':
        base_model = k.applications.EfficientNetB0(include_top=False, weights='imagenet')
    else:
        base_model = k.applications.InceptionV3(include_top=False, weights='imagenet')

    new_input = base_model.input
    hidden_layer = base_model.layers[-1].output

    image_features_extract_model = k.Model(new_input, hidden_layer)

    if plot:
        image_features_extract_model.summary()

    print(backbone, 'loaded')
    return image_features_extract_model


def get_image_tensor(image_filepath):
    file_ext = os.path.splitext(image_filepath)[-1]
    print('input image file:', image_filepath, file_ext)

    if file_ext == '.png':
        return tf.io.decode_png(tf.io.read_file(image_filepath), channels=3, dtype=tf.dtypes.uint8, name=None)
    else:
        return tf.io.decode_image(tf.io.read_file(image_filepath), channels=None, dtype=tf.dtypes.uint8, name=None,
                                  expand_animations=False)


_image_features_extract_model = get_cnn_model(settings.CNN_BACKBONE)


def extract_feature_vector(tensor):
    # image = k.preprocessing.image.smart_resize(image, (299, 299))

    x = tf.expand_dims(tensor, axis=0)
    x = tf.cast(x, tf.float32)

    if settings.CNN_BACKBONE == 'Inception':
        x = k.applications.inception_v3.preprocess_input(x)
    else:
        x = k.applications.imagenet_utils.preprocess_input(x, mode='torch')

    print('input shape:', x.shape)

    start = time()
    o = _image_features_extract_model(x)
    print('output shape:', o.shape)
    print('feature extraction duration (sec):', time() - start)

    return np.array(tf.reduce_mean(o, (0, 1, 2)))


if __name__ == '__main__':
    fp = './sample/cog1_hq2.jpg'
    fv = extract_feature_vector(get_image_tensor(fp))

    print(fv.shape)
    print('All Done')
