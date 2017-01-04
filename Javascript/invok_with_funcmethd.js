function myFunc(a){
  return a;
}
/*var result = myFunc.call(result, 34, 55);
console.log(result);
*/


var data = [45]
var another  = myFunc.apply(another, data)
console.log(another);
