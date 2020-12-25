# -*- coding: utf-8 -*-
import requests
import json

import settings

headers = {
    'APIKey': settings.LEONARDO_APIKEY,
    'Accept': 'application/json',
    # 'content-type' : 'multipart/form-data'
}


def feature_extraction(files):
    resp = requests.post(settings.LEONARDO_IMAGEFEATUREEXTRACTION_APIURL, files=files, headers=headers)
    if resp.status_code == 200:
        return json.loads(resp.text)['predictions']
    else:
        print('feature_extraction exception:', resp.status_code, resp.text)
        return []


def similarity_scoring(vectors, num_similar_vectors=1):
    data = {"texts": json.dumps(vectors),
            "options": json.dumps({"numSimilarVectors": num_similar_vectors})}
    resp = requests.post(settings.LEONARDO_SIMILARITYSCORING_APIURL, data=data, headers=headers)
    if resp.status_code == 200:
        return json.loads(resp.text)['predictions']
    else:
        print('similarity_scoring exception:', resp.status_code, resp.text)
        return []
