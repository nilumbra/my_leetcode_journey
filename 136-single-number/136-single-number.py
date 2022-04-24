class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        a = 0
        for i in nums:
            a ^= i
        
        return a
            
        