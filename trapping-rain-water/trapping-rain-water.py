class Solution:
    def trap(self, height: List[int]) -> int:
        left = leftmax = 0
        right = rightmax = len(height) - 1
        sw = 0
        
        while left < right:
            if height[leftmax] < height[rightmax]:
                left += 1
                if height[left] < height[leftmax]:
                    sw += height[leftmax] - height[left]
                else:
                    leftmax = left
            else:
                right -= 1
                if height[right] < height[rightmax]:
                    sw += height[rightmax] - height[right]
                else:
                    rightmax = right
        
        return sw
                