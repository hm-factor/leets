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
    
    if(neg) {
        let posInt = parseInt(reverseStr);
        let answer = -1*posInt;
    } else {
        let answer = parseInt(reverseStr);
    }

    if(answer < ((-2)**31) || answer > 2**31) {
      return 0
    } else {
      return answer
    };
};