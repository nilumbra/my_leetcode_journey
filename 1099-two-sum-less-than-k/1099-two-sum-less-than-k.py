from bisect import bisect_left
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = -1
        for i, num in enumerate(nums):
            if num < k:
                target = k - num
                in_pos = bisect_left(nums, target)
                # print(num, nums[in_pos - 1])
                s = num + nums[in_pos - 1]
                if s < k and in_pos - 1 != i:
                    ans = max(s, ans)
                
        # print(ans)
        return ans