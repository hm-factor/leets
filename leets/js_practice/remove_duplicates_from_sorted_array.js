/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let curr_num = null;
  let count = 0;

  for (let i = 0; i < nums.length; i++) {
    if (curr_num !== nums[i]) {
      count++;
    }
  }

  return count;
};
