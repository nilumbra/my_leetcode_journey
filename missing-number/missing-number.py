class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {i for i in range(len(nums)+1)}
        for num in nums:
            table.remove(num)

        return table.pop()

