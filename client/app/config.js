const fs = require('fs');

var _config;

module.exports = {
    getConfigs: function() {
        if (!_config) {
            _config = JSON.parse(fs.readFileSync('./config.json'));
        }

        return _config;
    }
};