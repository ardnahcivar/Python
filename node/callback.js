var max_time = 1000

var doubler = function(v, callback){
  var wait = Math.floor(Math.random()*max_time)
  if(v%2){
      setTimeout(function(){
        callback(new Error('ODD Input'));
      },wait);
  }
  else{
      setTimeout(function(){
        callback(null,v*2,wait)
      },wait)
  }
}

var handle = function(err, results, time){
  if (err){
      console.log('ERROR '+err.message);
  }
  else{
      console.log('the results are '+results+' time is '+time);
  }
}

doubler(123,handle);
doubler(124,handle);
doubler(125,handle);
console.log('***************');

for(var i =0;i<999999;i++){
  doubler(i,function(err, results, time){
    if(err){
      console.log('in loop ERROR '+err.message);
    }
    else{
        console.log('in loop the results are '+results+' time is '+time);
    }
  });
}
module.exports.doubler = doubler;
module.exports.handle = handle;
