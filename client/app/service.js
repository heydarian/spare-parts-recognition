const req = require('request');
const fs = require('fs');

const config = require('./config');

module.exports = {
    featureExtraction,
    similarityScoring
};

const _configs = config.getConfigs();

const headers = {
    'Accept': 'application/json'
    // 'content-type' : 'multipart/form-data'
};

function featureExtraction(filename, filepath = './app/sample/') {
    console.log(filepath + filename);
    return new Promise((resolve, reject) => {
        req.post(_configs.GENERAL.CNN_SERVER_ENDPOINT + '/extract', {
            // formData: {
            //     files: fs.createReadStream(filepath + filename)
            // },
            // json: true, 
            headers: headers,
            body: fs.createReadStream(filepath + filename) // binary input payload
        }, (err, res, body) => {
            if (err) { reject(err); }
            resolve(body);
        });
    });
}

function dotp(x, y) {
    function dotp_sum(a, b) {
        return a + b;
    }
    function dotp_times(a, i) {
        return x[i] * y[i];
    }
    return x.map(dotp_times).reduce(dotp_sum, 0);
}

function similarityScoring(a, b) {
    return dotp(a, b) / (Math.sqrt(dotp(a, a)) * Math.sqrt(dotp(b, b)));
}
