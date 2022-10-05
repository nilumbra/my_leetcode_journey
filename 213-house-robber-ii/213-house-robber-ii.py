class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        
        
        
        # Rob first
        if nums[0] > nums[1]:
            __p = _p = nums[0]
        else:
            __p, _p = nums[0], nums[1]
            
        for i in range(2, len(nums) - 1):
            _p, __p = max(_p, __p + nums[i])  , _p
        
        robMax = _p
        # Rob first not
        __p, _p = 0, nums[1]
        for i in range(2, len(nums)):
            _p, __p = max(_p, __p + nums[i])  , _p
        
        robMax = max(robMax, _p)
        return robMax
        