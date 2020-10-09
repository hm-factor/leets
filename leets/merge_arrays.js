/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
  if (m === 0) {
    return nums2;
  } else if (n === 0) {
    return nums1;
  };

  if (nums1[0] === 0 && m === 1) {
    return nums2;
  } else if (nums2[0] === 0 && n === 1) {
    return nums2;
  };
  
  let i = 0;
  while (nums2.length > 0) {

    if (nums2[0] <= nums1[i]) {
      nums1.splice(i, 0, nums2[0]);
      nums1.pop();
      nums2.shift();
    } else if (nums2[0] > nums1[m - 1]) {
      let firstZero = nums1.indexOf(0);
      nums1.splice((firstZero), 0, nums2[0])
      nums1.pop();
      nums2.shift();
    };

    i++;
  };

  return nums1
};