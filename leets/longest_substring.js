/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    if (s.length <= 1) return s.length
    
    let store = {}
    let min = -1
    let sub = 0
    
    for (let [i] in s) {
        sub = Math.max(sub, i - min);
        min = (store[s[i]] > min) ? i : min;
        store[s[i]] = i;
        console.log(store, min, sub)
    }
    
    return sub
};