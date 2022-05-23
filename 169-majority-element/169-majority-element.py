class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mc = len(nums) // 2
        while True:
            x = random.choice(nums)
            if sum([1 for num in nums if num == x]) > mc:
                return x
        