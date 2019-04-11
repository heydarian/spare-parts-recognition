const express = require("express");
const fs = require('fs');
const http = require('http');
const https = require('https');

// ssl cert
const credentials = {
    key: fs.readFileSync('./cert/private.pem', 'utf8'),
    cert: fs.readFileSync('./cert/client.crt', 'utf8')
};

const app = express();
// static files
app.use('/', express.static('./public'));
app.use('/labels', express.static('./public/labels.html'));
app.use('/favicon', express.static('./favicon.ico'));
// app.use('/dist', express.static('./dist'));
// app.use('/node_modules', express.static('./node_modules'));

// photo library file path
app.use('/spr_img', express.static('../server/label/b1_items'));



// http / https server
var httpServer = http.createServer(app);
var httpsServer = https.createServer(credentials, app);

const PORT = 8080;
const SSLPORT = 9080;

httpServer.listen(PORT, () => {
    console.log('HTTP Server is running on port %s', PORT);
});
httpsServer.listen(SSLPORT, () => {
    console.log('HTTPS Server is running on port %s', SSLPORT);
});