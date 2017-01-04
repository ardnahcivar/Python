var http  = require('http');
var fs = require('fs')



http.createServer(function(request,response){
  response.writeHead(200,{'content-Type':'text/html'});
  if(request.url === '/input.txt'){
    fs.createReadStream(__dirname+'/input.txt').pipe(response);
  }
  else{
    response.end('go to hell');
  }
}).listen(9999,'localhost');
console.log('server is running');
/*
var options = {
  host:'www.google.com',
  path:'/',
  port:'80',
  method:'GET'
};

http.get(options,function(response){
  console.log(response.statusCode);
  response.pipe(process.stdout);
});
console.log('directory is '+__dirname+'\nname of file is '+__filename);

*/
