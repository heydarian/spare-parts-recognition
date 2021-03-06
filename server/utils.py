# -*- coding: utf-8 -*-
import json
import os

from numpy import dot
from numpy.linalg import norm

import settings


def load_labels():
    with open(settings.LABEL_JSON_FILEPATH, 'r', encoding='utf-8') as json_file:
        labels = json.load(json_file)

    return labels


def remove_file_ext(filename):
    return os.path.splitext(filename)[0]


def cosine_similarity(v1, v2):
    return dot(v1, v2) / (norm(v1) * norm(v2))


def euclidean_similarity(v1, v2):
    return norm(v1 - v2)
