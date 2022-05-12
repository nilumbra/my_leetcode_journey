class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisect_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] >= target:
                    if nums[pivot] == target and (pivot - 1 < left or nums[pivot - 1] < target): # sweet index or first element is target
                        return pivot
                    right = pivot - 1
                else:
                    left = pivot + 1
            return -1
        
        def bisect_right(nums, target):
            left, right = 0, len(nums)
            while left < right:
                pivot = (left + right) // 2
                if nums[pivot] <= target:
                    if nums[pivot] == target and (pivot + 1 >= right or nums[pivot + 1] > target): # sweet index
                        return pivot
                    left = pivot + 1
                else: # nums[pivot] > target
                    right = pivot
            return -1
        
        res = [-1, -1]
        res[0] = bisect_left(nums, target)
        if res[0] == -1:
            return res
        else:
            res[1] = bisect_right(nums, target)
            return res