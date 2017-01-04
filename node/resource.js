var resource = require('./event_emitter')

var r =   new resource.resource(99);

r.on('start',function(){
  console.log('it has started');
});

r.on('data',function(i){
  console.log('it is receiving data '+i);
});

r.on('end',function(){
  console.log('it is the end');
})
