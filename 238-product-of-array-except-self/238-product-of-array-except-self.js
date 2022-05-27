/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    // First pass: store prefix product in ans array
    // Second pass: use another variable to keep track of suffix product
    
    const ans = new Array(nums.length);
    var left = right = 1;
    for (const [i, num] of nums.entries()) {
        ans[i] = left;
        left *= num;
    }
    
    for (let i = nums.length - 1; i >= 0; i--) {
        ans[i] *= right;
        right *= nums[i];
    }
    
    return ans;
};