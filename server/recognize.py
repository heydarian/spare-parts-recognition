# -*- coding: utf-8 -*-
import os
import json

from time import time

import config
import utils

from leonardo import feature_extraction, similarity_scoring


def generate_items(archive=True):
    f_list = [f for f in os.listdir(config.LABEL_B1_FILEPATH) if os.path.splitext(f)[1] == '.jpg']
    print(f_list)

    if len(f_list) == 0:
        return

    for f in f_list:
        print('extracting:', f)
        file = {'files': open(config.LABEL_B1_FILEPATH + f, 'rb')}
        results = feature_extraction(file)

        if len(results) > 0:
            for r in results:
                name = utils.remove_file_ext(f)
                config.DICT_LABEL[name] = r['featureVectors']

    if len(config.DICT_LABEL) > 0:
        with open(config.LABEL_B1_FILEPATH + 'label.json', encoding='utf-8') as json_file:
            label = json.load(json_file)

        for k, v in config.DICT_LABEL.items():
            print(k, v)
            if k in label:
                label[k]['featureVectors'] = v

        with open(config.LABEL_JSON_FILEPATH, 'w', encoding='utf-8') as json_file:
            json.dump(label, json_file)


def load_generate_items():
    with open(config.LABEL_JSON_FILEPATH, 'r', encoding='utf-8') as json_file:
        config.DICT_LABEL = json.load(json_file)


def recognize_items(img_file_name, num_similar_vectors=config.THRESHOLD_NUM_SIMILAR):
    files = {'files': open(config.SAMPLE_FILEPATH + '/' + img_file_name, 'rb')}
    start = time()
    results = feature_extraction(files)
    print('Leonardo feature_extraction:', time() - start)

    if len(results) > 0 and 'featureVectors' in results[0]:
        fvs = results[0]['featureVectors']
        vectors = {"0": [{"id": img_file_name, "vector": fvs}],
                   "1": [{"id": k, "vector": v['featureVectors']} for k, v in config.DICT_LABEL.items()]}

        # start = time()
        # results = similarity_scoring(vectors, num_similar_vectors=num_similar_vectors)
        # print('Leonardo similarity_scoring:', time() - start)

        start = time()
        results = similarity_scoring_self(vectors, num_similar_vectors=num_similar_vectors)
        print('self-built similarity_scoring:', time() - start)
        print('results:', results)
        return results
    else:
        print('no feature vectors')
        return []


def similarity_scoring_self(v, num_similar_vectors=1):
    if len(v['0']) > 0 and len(v['1']) > 0:
        ret_values = []
        for a in v['0']:
            similar_vectors = [{'id': b['id'], 'score': utils.cosine_similarity(a['vector'], b['vector'])} for b in
                               v['1']]
            similar_vectors.sort(key=lambda x: x['score'], reverse=True)
            ret_values.append({'id': a['id'], 'similarVectors': similar_vectors[:num_similar_vectors]})
        return ret_values
    return []


def export_results(raw):
    if len(raw) > 0:
        results = []
        for r in raw:
            item = config.DICT_LABEL[r['id']]
            results.append({'code': r['id'], 'name': item['name'], 'price': item['price'], 'quantity': item['quantity'],
                            'score': r['score'], 'image': os.environ.get('LABEL_IMG_URL', config.LABEL_IMG_URL) + r['id'] + '.jpg'})
        return results
    else:
        return []


if __name__ == '__main__':
    generate_items()

    print('All Done')
