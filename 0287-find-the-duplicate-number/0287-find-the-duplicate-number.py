# Theorm: 
#   For n+1 integer array containing integer in the range [1, n] inclusive, 
#      cannot have every array[n] to hold exactly one `n`. 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Goal: "pigeonhole every integer until encounter a duplicate"
        curr = 0
        nxt = nums[curr]
        while nxt != nums[nxt]:
            curr, nums[nxt] = nums[nxt], nxt
            nxt = curr
            
        return nxt