/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    
    let left = 0,
        right = height.length - 1,
        leftmax = left,
        rightmax = right,
        waterContained = (height, l, r) => Math.min(height[l], height[r]) * (r - l);
    
    
    while (left < right) {
        // console.log(height[left], height[right])
        // console.log((waterContained(height, left, right)))
        // console.log(height[left+1], height[right-1])
        // console.log("----")
        if (height[left] < height[right]) {
            left++;
            // console.log(waterContained(height, left, rightmax), waterContained(height, leftmax, rightmax))
            if(waterContained(height, left, rightmax) > waterContained(height, leftmax, rightmax)) {
                leftmax = left;
            }
            
        } else {
            right--;
            // console.log(waterContained(height, left, rightmax), waterContained(height, leftmax, rightmax))
            if(waterContained(height, leftmax, right) > waterContained(height, leftmax, rightmax)) {
                rightmax = right;
            }
        }
        
        if(waterContained(height, left, right) > waterContained(height, leftmax, rightmax)) {
            rightmax = right,
            leftmax = left
        }
    }
    
    return waterContained(height, leftmax, rightmax)
};