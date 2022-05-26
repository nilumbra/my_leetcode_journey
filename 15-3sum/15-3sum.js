/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    
    const compFn = (a, b) => a - b;
    const seen = new Set();
    nums.sort(compFn);
    
    console.log(nums)
    const ans = [];
    for (const [idx, target] of nums.entries()) {
        const twoSumsAns = twoSum(nums.slice(idx + 1), -target)
        // console.log("Target: " + (-target))
        // twoSumsAns.forEach(item => {
        //     console.log([item[0] + idx + 1, item[1] + idx + 1])
        // })
        for (const [_, __] of twoSumsAns) {  
            //nums[_] + nums[__] == -target, i.e. they sum to 0
            const triplet = [nums[_ + idx + 1], nums[__ + idx + 1], target];
            triplet.sort(compFn);
            const triplet_srl = JSON.stringify(triplet);
            if (!seen.has(triplet_srl)){
                ans.push(triplet);
                seen.add(triplet_srl);
            }
        }
    }
    
    return ans;
};


var twoSum = function(numbers, target) {
    var left = 0, 
        right = numbers.length - 1;

    const ans = [];
    while (left < right) {
        if (numbers[left] + numbers[right] > target) {
            right--;
        } else if (numbers[left] + numbers[right] < target) {
            left++;
        } else {
            ans.push([left, right])
            if (numbers[left + 1] + numbers[right] > target) {
                right--;
            } else {
                left++;
            }
        }
    }

    return ans;
};
