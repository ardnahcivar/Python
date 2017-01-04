process.stdin.resume();
process.stdin.setEncoding('utf8');

process.stdin.on('data',function(d){
      process.stdout.write('data is ->'+d);
});

process.stdin.on('end',function(){
    process.stderr.write('terminated\n');
});
