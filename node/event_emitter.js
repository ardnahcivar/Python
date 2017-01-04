var events = require('events').EventEmitter;
var util = require('util');


function resource(c){
  var max = c;
  var self = this;
  process.nextTick(function(){
    var count = 0;
    self.emit('start');
    var t = setInterval(function(){
        //console.log('time interval is ');
        self.emit('data',count++);
        if(count === max)
        {
            self.emit('end',count);
            clearInterval(t);
        }
    },10);
  });
  //console.log('checking it  out'+e);
}

util.inherits(resource,events);
module.exports.resource = resource;
