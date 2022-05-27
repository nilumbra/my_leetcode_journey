/**
 * @param {number[]} nums
 * @return {boolean}
 */


// If curr element is greater than the last, append
// else if it is smaller than the last one, 

var isIncreasing = function (arr) {
    if (arr.length === 1 || (arr.length === 2 && arr[0] < arr[1])) {
        return true
    }
    return false;
}

var increasingTriplet = function(nums) {
    const ans = [nums[0]];
    for (const num of nums.slice(1)) {
        if (num > ans.at(-1) ) { // append
            ans.push(num);
            if (ans.length === 3) {
                return true
            }
        } else if (num < ans.at(-1)) {
            // update the last element greedily
            if (ans.length === 2) {
                // ans.length = 2 && ans[-2] < num
                if (num < ans.at(-2)) {  // e.g. ans = [2, 3], num = 1
                    ans[0] = num;
                } else if (num < ans[1] && num > ans[0]) { // e.g. ans = [1, 3], num = 2
                    ans[1] = num;    
                }
            } else { // ans.length == 1
                ans[0] = num;
            }
        }
        // console.log(ans)
    }
    
    return false;
};