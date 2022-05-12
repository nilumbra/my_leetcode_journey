/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {
    function isSubsetSum(arr, target){
  var [m, n] = [arr.length + 1, target + 1];
  var dp = []; 

  // set dp to be an (m by n) 2D-array
  for (let i = 0; i < m; i++) {
    dp.push(new Array(n).fill(false));
  }

  // initialize dp;

  // when the target sum is 0; just pick none of the element from the array
  // ,that is, for all 1 <= i <= m, arr[0:i] can sum to 0; hence ==>
  for (let i = 0; i < m; i++) {
    dp[i][0] = true;
  }

  // arr[0:0] is empty set, i.e. arr[0:0] can't sum to any number j, for 1 <= j < n;
  for (let j = 1; j < n; j++) {
    dp[0][j] = false;
  }

  // console.log(dp)

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (j < arr[i - 1]) { // if the target number j is smaller than current num, then it's impossible that by adding the current number to the sum set we get the target number; hence dp[i][j] completely depends on dp[i - 1][j]
        dp[i][j] = dp[i - 1][j];
      } else {
        dp[i][j] = dp[i - 1][j] || dp[i - 1][j - arr[i - 1]];
        // if (typeof dp[i][j] === 'undefined') {
        //   console.log(`dp[${i}][${j}] should not be undefined!!!`)
        //   console.log(`dp[${i - 1}][${j}] = ${dp[i - 1][j]}`)
        //   console.log(`dp[${i - 1}][${j - arr[i - 1]}] = ${dp[i - 1][j - arr[i - 1]]}`)
        // }
      }

      if (j === target && dp[i][j]) {
        return true;
      }
    }
  }
  return false
  // return -1
}

   const target = nums.reduce((acc, curr) => (acc + curr)) / 2;
    console.log(target)
   if (!Number.isInteger(target)) {
       // console.log("Target is not integer; false")
       return false;
   } else{
       return isSubsetSum(nums, target)
   }
};