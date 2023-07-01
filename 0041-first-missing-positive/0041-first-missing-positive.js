// array of length n, first missing positive integer
//   max: n + 1
//   min: 1


/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    const n = nums.length
    const [min, max] = [1, n + 1]
    
    if(!nums.some(num => num === 1)) return 1 // if there's no 1 in the array then the answer is 1
    
    // preprocessing, does not affect the answer
    nums = nums.map(num => (num < min || num >= max) ? 1 : num)
    
    // use nums[0]'s sign to keep track of whether `n` is in the array
    for (let i in nums) {
        const pos = Math.abs(nums[i]) % n
        if (nums[pos] > 0) {
            nums[pos] = -nums[pos]
        }
    }
    // console.log(nums)

    for (let i = 1; i <= n; i++) {
        if (nums[i % n] > 0) return i
    }    
    console.log("shouldn't reach here", nums)
    return n + 1
};