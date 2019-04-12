const req = require('request');
const fs = require('fs');

module.exports = {
    featureExtraction,
    similarityScoring
};

const LEONARDO_APIKEY = 'jGMB8R9KPK2MhNv7Tc9vTVGQ1mu7KLB0'
const LEONARDO_IMAGEFEATUREEXTRACTION_APIURL = 'https://sandbox.api.sap.com/ml/imagefeatureextraction/feature-extraction'
const LEONARDO_SIMILARITYSCORING_APIURL = 'https://sandbox.api.sap.com/ml/similarityscoring/similarity-scoring'

const headers = {
    'APIKey': LEONARDO_APIKEY,
    'Accept': 'application/json'
    // 'content-type' : 'multipart/form-data'
}

function featureExtraction(filename) {
    return new Promise((resolve, reject) => {
        req.post(LEONARDO_IMAGEFEATUREEXTRACTION_APIURL, {
            formData: {
                files: fs.createReadStream('./app/sample/' + filename)
            },
            json: true,
            headers: headers
        }, (err, res, body) => {
            if (err) { reject(err); }
            resolve(body);
        });
    });
}

function similarityScoring(vectors, numSimilarVectors = 1) {
    return new Promise((resolve, reject) => {
        req.post(LEONARDO_SIMILARITYSCORING_APIURL, {
            formData: {
                texts: JSON.stringify(vectors),
                options: JSON.stringify({ "numSimilarVectors": numSimilarVectors })
            },
            json: true,
            headers: headers
        }, (err, res, body) => {
            if (err) { reject(err); }
            resolve(body);
        });
    });
}

