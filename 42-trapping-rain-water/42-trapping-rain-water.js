/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    /*
     use two pointer to delineate the boundary of a consecutive body of trapped rain

     e.g. 
     [1,2,3,4,3,2,3]
    */
    
    var leftmax = left = 0,
        rightmax = right = height.length - 1,
        ans = 0;
    
    while (left < right) {
        if (height[left] <= height[right]) {
            // UPDATE LEFT
            if (height[left] >= height[leftmax]) {
                leftmax = left;
            } else {
                ans += height[leftmax] - height[left];
            }
            console.log("left", ans)
            left++;
        } else {
            // UPDATE RIGHT
            if (height[right] >= height[rightmax]) {
                rightmax = right;
            } else {
                ans += height[rightmax] - height[right];
            }
            
            // console.log("right", right, "rightmax", rightmax, "ans", ans)
            
            right--;
        }
    }
    
    return ans
};