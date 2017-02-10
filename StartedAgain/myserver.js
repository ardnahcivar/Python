var fs = require('fs')
var url = require('url')
var http = require('http')

http.createServer(function(request,response){
    var pathname = url.parse(request.url).pathname;
    fs.readFile(pathname.substr(1),function(err,data){
      if(err){
        console.log('INVALID FILE');
        response.writeHead(404,'{Content-Type:text/html}')
        response.write('<h1>Resource Not Found</h1>')
      }
      else{
        console.log('File Found');
        response.writeHead(200,'{Content-Type:text/html}');
        response.write(data.toString())
      }
    })

}).listen(8090);
