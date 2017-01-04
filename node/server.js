var http = require('http')
var make_server = function(){
http.createServer(function(req,res){
res.writeHead(200,{'content-Type':'text/html'});
res.end('<h1>Hello</h1>');
}).listen(1337);
console.log('server running');
}
module.exports.make_server = make_server;
