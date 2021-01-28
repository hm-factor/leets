function selectionSort(arr) {
  // base case of empty array
  if(arr.length === 0) return arr;

  // subarrays
  let copy = arr;
  let sorted = [];

  // while sub2 has length > 1
  while (sorted.length !== arr.length) {
    // find min value
    let min = Math.min(...copy);
    // push into sorted
    sorted.push(min);
    // remove value from copy, indexOf, slice
    let idx = copy.indexOf(min);
    copy[idx] = null;
  }

  // return sub1
  return sorted;
}

console.log(selectionSort([64, 25, 12, 22, 11]));

// [] copy
// [11, 12, 22, 25, 64] sorted

// selection sort
// sorts alg finds min element and puts at beginning, two subarray
// sub1: every iteration, min goes to sorted subarray (sorted)
// sub2: original array w els removed (copy)

// check for empty array
// could have duplicates
