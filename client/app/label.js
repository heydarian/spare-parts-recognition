const fs = require('fs');
const req = require('request');

var _itemLabels;

module.exports = {
    updateLabels: function(e) {
        console.log(e);
    },
    getLabels: function () {
        if (!_itemLabels) {
            _itemLabels = JSON.parse(fs.readFileSync('./app/label/labels.json'));
        }

        return _itemLabels;
    }
}