/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    if(n === 0) return [];
    
    let ok = new Set;
    let str = "(";
    
    addParens(str, 1, 0, ok, n);
    
    return Array.from(ok);
    
};
// recursively call add parenthesis with both left and right, until you run out of left and right
//  helper method should add a left or right parens and decrement the appropriate 

function addParens (str, l, r, mySet, n) {
    if (str.length === n*2) {
        mySet.add(str);
        return
    }
    if (l < n && str.length < n*2) {
        addParens(str + "(", l+1, r, mySet, n);      
    }
    if (r < l && str.length < n*2) {
        addParens(str + ")", l, r+1, mySet, n);            
    }
}
