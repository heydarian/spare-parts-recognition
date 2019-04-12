const fs = require('fs');
const leon = require('./leonardo');
const label = require('./label')

module.exports = {
    search: searchImage,
    score: similarityScoring,
    export: exportResult
};

async function searchImage(filename, numSimilarVectors = 3) {
    var result = await leon.featureExtraction(filename);
    //console.log('searchImage:', result);

    if (result && result.hasOwnProperty('predictions') && result.predictions[0].hasOwnProperty('featureVectors')) {
        const labels = label.getLabels();
        var condinates = [];

        for (let k in labels) {
            condinates.push({ "id": k, "vector": labels[k].featureVectors });
        }

        const vectors = {
            "0": [{ "id": filename, "vector": result.predictions[0].featureVectors }],
            "1": condinates
        };

        // console.log(vectors);

        return await leon.similarityScoring(vectors, numSimilarVectors);
    } else {
        return [];
    }
}

function similarityScoring(v, num_similar_vectors = 1) {
    // if len(v['0']) > 0 and len(v['1']) > 0:
    //     ret_values = []
    //     for a in v['0']:
    //         similar_vectors = [{'id': b['id'], 'score': utils.cosine_similarity(a['vector'], b['vector'])} for b in
    //                            v['1']]
    //         similar_vectors.sort(key=lambda x: x['score'], reverse=True)
    //         ret_values.append({'id': a['id'], 'similarVectors': similar_vectors[:num_similar_vectors]})
    //     return ret_values
    // return []

    return;
}

function exportResult(raw) {
    // if len(raw) > 0:
    //     results = []
    //     for r in raw:
    //         item = config.DICT_LABEL[r['id']]
    //         results.append({'code': r['id'], 'name': item['name'], 'price': item['price'], 'quantity': item['quantity'],
    //                         'score': r['score'], 'image': config.LABEL_IMG_URL + r['id'] + '.jpg'})
    //     return results
    // else:
    //     return []
    return;
}
