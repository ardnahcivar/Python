/*var fs = require("fs");
var data  = '';
var readStream  = fs.createReadStream('input.txt');
readStream.setEncoding('UTF8');

readStream.on('data',function(d){
  data  += d;
})

readStream.on('end',function(){
  console.log('Data is :'+data);
  writeStream.write(data,'UTF8');
  //writeStream.end();
})

readStream.on('error',function(error){
  console.log('got an error'+error.stack);
})



var writeStream  = fs.createWriteStream('output.txt')


writeStream.on('finish',function(){
  console.log('writing finished');
})



writeStream.on('error',function(){
  console.log(error.stack);
})


console.log(__filename);
console.log(__dirname);


function sayHello(){
  console.time('time is :')
  console.log('hey');
  console.timeEnd('time is :');
}

setInterval(sayHello,2000);
*/

console.log(process.execPath);
console.log(process.platform);
console.log(process.memoryUsage());
console.log(process.cwd());
console.log(process.version);
