const hostname = '127.0.0.1'; //pvgm50898582a.dhcp.pvgl.sap.corp
const config = {
    'NODE_SERVER_ACTIVE': false,
    'PYTHON_SERVER_PATH': `${window.location.protocol}//${hostname}:${window.location.protocol == 'http:' ? '8005' : '9005'}/api`,
};

function getServerAddress() {
    return !config.NODE_SERVER_ACTIVE ? config.PYTHON_SERVER_PATH : '/api';
}