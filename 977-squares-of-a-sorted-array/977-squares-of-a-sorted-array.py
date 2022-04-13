class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        left, right = 0, n - 1
        
        for i in range(n - 1, -1, -1):
            # Get the greater square of two sides
            if abs(nums[left]) >= abs(nums[right]): 
                square = nums[left]
                left += 1
            else:
                square = nums[right]
                right -= 1
                
            output[i] = square * square
        
        return output
            
            
        