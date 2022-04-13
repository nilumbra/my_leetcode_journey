class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_zero = -1
        for i,n in enumerate(nums):
            if n == 0:
                left_zero = i if left_zero == -1 else left_zero
                # print("called", i, n, left_zero)
            else:
                if left_zero != -1: 
                    nums[i] = 0
                    nums[left_zero] = n
                    left_zero += 1
            
                