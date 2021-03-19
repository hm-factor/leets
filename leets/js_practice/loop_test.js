// let test_arr = [1,2,3,4]

// const loopTest = (arr) => {
//   for(let i = 0; i < arr.length; arr[i]%2 ? i++ : i+=2){
//     console.log(arr[i])
//     arr[i]+=1
//   }
//   return arr
// } 

// console.log(loopTest(test_arr))

intervals = [[1,3],[8,10],[15,18],[2,6],[1,2],[1,5]]

intervals.sort((a,b) => a[0] - b[0])

console.log(intervals)