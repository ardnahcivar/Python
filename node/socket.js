var http = require('http')
var socketio = require('socket.io')
var fs = require('fs')


var app = http.createServer(function(request,response){
    fs.readFile(__dirname+'/index.txt')

});
