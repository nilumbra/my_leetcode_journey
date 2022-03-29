class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        for i in range(len(nums) + 1):
            s += i
            
        for num in nums:
            s -= num

        return s

