# -*- coding: utf-8 -*-
LABEL_B1_FILEPATH = './labels/b1_items/'
LABEL_OTHER_FILEPATH = './labels/other_items/'
LABEL_JSON_FILEPATH = './labels/labels.json'
LABEL_IMG_URL = 'http://127.0.0.1:8085/spr_img/'

SAMPLE_FILEPATH = './samples/'

CNN_BACKBONE = 'Inception'  # Densenet, Efficientnet
THRESHOLD_SIMILAR = 0.65
THRESHOLD_NUM_SIMILAR = 3

MULTI_PROCESSES_MODE = False
NUM_PROCESSES = 2

LEONARDO_APIKEY = 'jGMB8R9KPK2MhNv7Tc9vTVGQ1mu7KLB0'
LEONARDO_IMAGEFEATUREEXTRACTION_APIURL = 'https://sandbox.api.sap.com/ml/imagefeatureextraction/feature-extraction'
LEONARDO_SIMILARITYSCORING_APIURL = 'https://sandbox.api.sap.com/ml/similarityscoring/similarity-scoring'
