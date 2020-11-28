/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {

    if (s.length <= 1) return s.length;
    
    let store = {}
    let min = 0
    let sub = 0
    
    for (let [i] in s) {
        let idx = parseInt(i)
        sub = Math.max(sub, idx - min);
        min = (store[s[i]] >= min) ? idx : min;
        store[s[i]] = i;
    }
    
    return sub;
};