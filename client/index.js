const express = require("express");
const bodyParser = require("body-parser");

const fs = require('fs');
const http = require('http');
const https = require('https');

const label = require('./app/label');
const recognize = require('./app/recognize');
const utils = require('./app/utils');

// ssl cert
const credentials = {
    key: fs.readFileSync('./cert/private.pem', 'utf8'),
    cert: fs.readFileSync('./cert/client.crt', 'utf8')
};

const app = express();
app.use(bodyParser.json());

// static files
app.use('/', express.static('./public'));
app.use('/labels', express.static('./public/labels.html'));
app.use('/favicon', express.static('./favicon.ico'));
// app.use('/dist', express.static('./dist'));
// app.use('/node_modules', express.static('./node_modules'));

// photo library file path
app.use('/spr_img', express.static('../server/label/b1_items'));

// initial labels
console.log('labels loaded');
// console.log('labels loaded:\n', label.getLabels());

app.post('/api/recognize',  async function (req, res, next) {
    if (!req.body || !req.body.hasOwnProperty('filename') || !req.body.hasOwnProperty('image')) {
        res.sendStatus(400);
    }

    var filename = req.body.filename;
    console.log('input:', req.body.filename);

    let base64Data = req.body.image.replace(/^data:image\/png;base64,/, '').replace(/^data:image\/jpeg;base64,/, '');
    // let contentType = req.body.image.substring(0, req.body.image.indexOf(';base64,'));
    // let blob = utils.b64toBlob(base64Data, contentType);

    fs.writeFileSync('./app/sample/' + filename, base64Data, 'base64', function (err) {
        next(err);
        res.sendStatus(415);
    });

    var results = await recognize.search(filename);
    // filename = utils.remove_file_ext(input_data['filename'])

    // results = recognize_items(input_data['filename'])


    // if len(results) > 0 and 'similarVectors' in results[0]:
    //     ret_data = [r for r in results[0]['similarVectors'] if r['score'] >= config.THRESHOLD_SIMILAR]

    //     ### hardcode required by Darius
    //     if config.FLAG_HARDCODE:
    //         fake_ret_data = []
    //         for r in ret_data:
    //             if r['id'].upper() == 'CW0001':
    //                 fake_ret_data.append({'id': 'CW0001', 'score': random.uniform(0.92, 0.98)})
    //             else:
    //                 fake_ret_data.append(r)
    //         ret_data = fake_ret_data
    //     ###

    //     ret_data.sort(key=lambda x: x['score'], reverse=True)
    //     resp = json.dumps({"state": "success", "filename": filename, "data": export_results(ret_data)})

    // TODO
    if (true) {
        res.send({ "state": "success", "filename": filename, "data": results });
    } else {
        // next('error');
        res.sendStatus(204);
    }
});


// http / https server
var httpServer = http.createServer(app);
var httpsServer = https.createServer(credentials, app);

const PORT = 8080;
const SSLPORT = 9080;

httpServer.listen(PORT, () => {
    console.log('HTTP Server is running on port %s', PORT);
    console.log('-'.repeat(100));
});

httpsServer.listen(SSLPORT, () => {
    console.log('HTTPS Server is running on port %s', SSLPORT);
    console.log('-'.repeat(100));
});

