/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    seen = {}
    for (const [i, v] of nums.entries()) {
        if (v in seen) {
            return [seen[v], i]
        }
        
        seen[target - v] = i
    }
};