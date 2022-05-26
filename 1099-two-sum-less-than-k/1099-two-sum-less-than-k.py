from bisect import bisect_left
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = -1
        for i, num in enumerate(nums):
            if num >= k:
                break
            else:
                in_pos = bisect_left(nums, k - num, i + 1) - 1
                if in_pos > i:
                    ans = max(num + nums[in_pos], ans)
                
        # print(ans)
        return ans