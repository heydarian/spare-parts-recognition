const fs = require('fs');

const config = require('./config');
const service = require('./service');
const label = require('./label');

module.exports = {
    search: searchImage,
    export: exportResult
};

const _configs = config.getConfigs();

async function searchImage(filename) {
    var result = await service.featureExtraction(filename);
    result = JSON.parse(result); // Convert to JSON
    console.log('feature extraction:', result);

    if (result && result.hasOwnProperty('state') && result.state == 'success' && result.hasOwnProperty('data')) {
        var candidates = [];
        const labels = label.getLabels();
        for (let k in labels) {
            score = service.similarityScoring(result.data, labels[k].featureVectors);
            console.log(k, score);
            if (score >= _configs.GENERAL.THRESHOLD_SIMILAR) {
                candidates.push({ "id": k, "score": score });
            }
        }

        candidates.sort((a, b) => { return b.score - a.score; });
        // console.log('similarity scoring (TOP N):', candidates);

        return candidates.slice(0, _configs.GENERAL.THRESHOLD_NUM_SIMILAR);
    } else {
        return [];
    }
}


function exportResult(raw) {
    var results = [];
    for (let r of raw) {
        let item = label.getLabels(r.id);
        if (item) {
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

    results.sort((a, b) => { return b.score - a.score; });
    return results;
}
