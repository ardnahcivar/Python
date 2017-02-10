var express = require('express')
var app = express()
app.use(express.static('Myfiles'));

app.get('/',function(request,response){
  response.sendFile(__dirname+'/'+'input.html');
})

.get('/images_get',function(request,response){
    response.write('<h1>HEY</h1>')
})

.use(function(request,response,next){
  response.setHeader(404,'Content-Type:text/html');
  response.end('<h4>resource not found<h4>');
})

var server  = app.listen(8081,function(){
  var host = server.address().host;
  var port = server.address().port;
  console.log('server started');
})
