/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows === 1) return s;    
    let arr = new Array(numRows);
    let count = 0;
    
    for(let i = 0; i < s.length; i++;) {
        let idx = i % numRows;
        if (arr[idx] === undefined) {
            arr[idx] += ""
        }    
    }
    
};
