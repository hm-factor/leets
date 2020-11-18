/**
 * @param {number} x
 * @return {number}
 */

var reverse = function(x) {
   if(x === 0) return 0;

       
    let neg = false;
    
    if(x < 0) { neg = true };
    
    let temp = x.toString();
    let arr = temp.split("");
    if(arr[0] === '-') {arr.shift()}
    
    
};