class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums = sorted(nums)
        previous = None 
        for (idx, el) in enumerate(nums):
            if (previous == el): continue
            for idx1, idx2 in two_sum(nums[idx + 1:], -el):
                ans.append([el, nums[idx1 + idx + 1], nums[idx2 + idx + 1]])
            previous = el
        return ans 
        
def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1
    ans = []
    while left < right:
        # print(left, right)
        if numbers[left] + numbers[right] == target: 
            ans.append((left, right))
            while left < right and numbers[left+1] == numbers[left]:
                left += 1
            while left < right and numbers[right-1] == numbers[right]:
                right -= 1
        if (numbers[left] + numbers[right]) > target:
            right -= 1
        else:
            left += 1

    return ans