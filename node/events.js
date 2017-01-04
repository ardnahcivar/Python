var events = require('events').EventEmitter;

var resource = function(c){
  var e = new events();
  process.nextTick(function(){
    var count = 0;
    e.emit('start');
    var t =setInterval(function(){
        console.log('time interval is ')  ;
        e.emit('data',count++);
        if(count === c)
        {
            e.emit('end',count);
            clearInterval(t);
        }
    },10);
  });
  console.log('checking it  out'+e);
  return(e);

}

var r = resource(13);
r.on('start',function(){
  console.log('it has started');
})

r.on('data',function(i){
  console.log('FFFF'+i);
})

r.on('end',function(){
  console.log('it is the end');
})
