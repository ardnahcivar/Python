var os = require('os')
//var call_back = require('./callback')
var server = require('./server')
console.log(os.hostname());
console.log(os.freemem());
console.log(os.arch());
console.log(os.endianness());
console.log(os.uptime());
console.log(os.networkInterfaces());
console.log(os.loadavg()[2]);
console.log(server.make_server());
