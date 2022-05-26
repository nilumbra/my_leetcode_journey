class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        _0__f = 0
        f__2 = len(nums) - 1
        curr = 0
        
        while curr <= f__2:
            if nums[curr] == 2:
                nums[curr], nums[f__2] = nums[f__2], nums[curr]
                f__2 -= 1
            else:
                if nums[curr] == 0:
                    nums[curr], nums[_0__f] = nums[_0__f], nums[curr]
                    _0__f += 1
                
                curr += 1
        