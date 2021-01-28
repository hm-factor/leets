/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
  if (a === '0' && b === '0') return "0";

  let output = [];
  let len = 0;
  let carry = 0;

  if (a.length > b.length) {
    len = a.length
  } else {
    len = b.length
  };

  let a_rev = a.split('').reverse();
  let b_rev = b.split('').reverse();

  let i = 0;

  while (a_rev[i] || b_rev[i] || carry > 0) {

    let x = a_rev[i] ? parseInt(a_rev[i]) : 0;
    let y = b_rev[i] ? parseInt(b_rev[i]) : 0;

    let num = x + y + carry;

    if (num === 0 || num === 1) {
      output.push(num);
      carry = 0;
    } else if (num === 2) {
      output.push(0);
      carry = 1;
    } else {
      output.push(1);
      carry = 1;
    };

    i++;
  };

  return output.reverse().join('');
};