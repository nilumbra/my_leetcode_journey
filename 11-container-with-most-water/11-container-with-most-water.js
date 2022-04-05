/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    
    let left = 0,
        right = height.length - 1,
        waterContained = (height, l, r) => Math.min(height[l], height[r]) * (r - l),
        maxArea = waterContained(height, left, right);
    
    
    while (left < right) {
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
        
        let area = waterContained(height, left, right);
        maxArea = area > maxArea ? area: maxArea;
    }
    return maxArea
};