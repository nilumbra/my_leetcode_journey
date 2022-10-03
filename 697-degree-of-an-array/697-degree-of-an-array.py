from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        memo = defaultdict(lambda: [0, 0, 0]) # [freq, start, end]
        degree = 0
        for i, num in enumerate(nums):
            if not memo[num][0]: # if <num> is a first encounter, remember <i> as the start position for <num>
                memo[num][1] = i
                
            memo[num][0] = memo[num][0] + 1
            memo[num][2] = i
            
            # If is curr. max...
            if memo[num][0] > degree:
                degree = memo[num][0]
            
        ans = len(nums)
        for freq, start, end in memo.values():
            if degree == freq:
                ans = min(ans, end - start + 1)

        return ans
            
            
                