const fs = require('fs');

const leon = require('./leonardo');
const label = require('./label')

module.exports = {
    search: searchImage,
    score: similarityScoring,
    export: exportResult
};

const _labels = label.getLabels();

async function searchImage(filename, numSimilarVectors = 3) {
    var result = await leon.featureExtraction(filename);
    console.log('feature extraction:', result);

    if (result && result.hasOwnProperty('predictions') && result.predictions[0].hasOwnProperty('featureVectors')) {
        var condinates = [];
        for (let k in _labels) {
            condinates.push({ "id": k, "vector": _labels[k].featureVectors });
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

function similarityScoring(v, numSimilarVectors = 1) {
    // if len(v['0']) > 0 and len(v['1']) > 0:
    //     ret_values = []
    //     for a in v['0']:
    //         similar_vectors = [{'id': b['id'], 'score': utils.cosine_similarity(a['vector'], b['vector'])} for b in
    //                            v['1']]
    //         similar_vectors.sort(key=lambda x: x['score'], reverse=True)
    //         ret_values.append({'id': a['id'], 'similarVectors': similar_vectors[:numSimilarVectors]})
    //     return ret_values
    // return []

    return;
}

function exportResult(raw) {
    var results = [];
    for (r of raw) {
        if (_labels.hasOwnProperty(r.id)) {
            let item = _labels[r.id];
            results.push({
                code: r.id,
                name: item.name,
                price: item.price,
                quantity: item.quantity,
                score: r.score,
                image: `/library/${r.id}.jpg`
            });
        }
    }
    return results;
}
