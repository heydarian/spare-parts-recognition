# -*- coding: utf-8 -*-
import json
import os

import numpy as np

import settings
import utils
from service import get_image_tensor, extract_feature_vector

_labels = utils.load_labels()
print('labels loaded:', len(_labels))


def generate_labels(archive=True):
    file_list = [f for f in sorted(os.listdir(settings.LABEL_B1_FILEPATH)) if
                 os.path.splitext(f)[-1] in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']]
    # print(file_list)

    if len(file_list) == 0:
        return

    for fp in file_list:
        name = utils.remove_file_ext(fp).upper()
        print('extracting:', fp)

        fv = extract_feature_vector(get_image_tensor(settings.LABEL_B1_FILEPATH + fp))
        print('feature vectors:', list(fv.astype(float)))

        if name in _labels:
            _labels[name]['featureVectors'] = list(fv.astype(float))
            print(name, 'extracted')

        print('-' * 20)

    with open(settings.LABEL_JSON_FILEPATH, 'w', encoding='utf-8') as f:
        json.dump(_labels, f)

    return _labels


def find_similar_items(fv, threshold_similar=0.6, num_similar_vectors=3):
    if len(_labels) <= 0:
        return []

    results = []
    for k, v in _labels.items():
        score = utils.cosine_similarity(fv, np.array(v['featureVectors'], dtype='float32'))
        if score >= threshold_similar:
            results.append((k, score))

    return sorted(results, key=lambda x: x[1], reverse=True)[:num_similar_vectors]


def process(img_file_name):
    fp = settings.SAMPLE_FILEPATH + img_file_name
    fv = extract_feature_vector(get_image_tensor(fp))

    return find_similar_items(fv, settings.THRESHOLD_SIMILAR, settings.THRESHOLD_NUM_SIMILAR)


def export_results(raw):
    results = []
    if len(raw) > 0:
        for r in raw:
            key, score = r
            item = _labels[key]
            results.append({'code': key, 'name': item['name'], 'price': item['price'], 'quantity': item['quantity'],
                            'score': float(score),
                            'image': os.environ.get('LABEL_IMG_URL', settings.LABEL_IMG_URL) + key + '.jpg'})
    return results


if __name__ == '__main__':
    # generate_labels()

    items = process('cog1_hq2.jpg')

    print(export_results(items))
    print('All Done')
