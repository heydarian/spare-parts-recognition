require('dotenv').config();

module.exports = {
    getConfigs: function () {
        return {
            "GENERAL": {
                "THRESHOLD_SIMILAR": Number(process.env.GENERAL_THRESHOLD_SIMILAR),
                "THRESHOLD_NUM_SIMILAR": Number(process.env.GENERAL_THRESHOLD_NUM_SIMILAR),
                "DATASETS": "all".toLowerCase(),
                "CNN_SERVER_ENDPOINT": process.env.CNN_SERVER_ENDPOINT,
            },
            "BUSINESSONE": {
                "SERVICELAYER_APIURL": process.env.B1_SERVICELAYER_APIURL,
                "USERNAME": process.env.B1_USERNAME,
                "PASSWORD": process.env.B1_PASSWORD,
                "COMPANYDB": process.env.B1_COMPANYDB,
            },
            "BYDESIGN":{
                "TENANT_HOSTNAME": process.env.BYD_TENANT_HOSTNAME,
                "USERNAME": process.env.BYD_USERNAME,
                "PASSWORD": process.env.BYD_PASSWORD,
            }
        };
    }
};