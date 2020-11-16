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
    
    let newArr = [];
    for(let i=arr.length; i--; i >= 0) {
        newArr.push(arr[i]);
    }
    
    let reverseStr = newArr.join("")

    let newAnswer = 0;
    
    if(neg) {
        let posInt = parseInt(reverseStr);
        newAnswer = -1*posInt;
    } else {
        newAnswer = parseInt(reverseStr);
    }

    if(newAnswer < ((-2)**31) || newAnswer > 2**31) {
      return 0
    } else {
      return newAnswer
    };
};