/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    var m = -Infinity;
    
    for (let l = 0, r = height.length - 1; l < r;) {
        m = Math.max(Math.min(height[l], height[r]) * (r - l), m);
        height[l] < height[r] ? l++: r--;
    }
    
    return m
};