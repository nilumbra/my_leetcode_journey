class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for (idx, v) in enumerate(nums):
            diff = target - v
            if diff in seen:
                return [idx, seen[diff]]
            
            seen[v] = idx