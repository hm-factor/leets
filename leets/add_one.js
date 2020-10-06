/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  let bigNum = parseInt(digits.join(''));
  bigNum = bigNum + 1;
  let newDig = String(bigNum).split('');
  return newDig;
};