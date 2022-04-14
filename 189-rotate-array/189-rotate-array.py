class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k >= n:
            k %= n
            
        unchanged = nums[0:n-k]
        changed = nums[n-k:]
        nums[:] = changed + unchanged 
        
            
        