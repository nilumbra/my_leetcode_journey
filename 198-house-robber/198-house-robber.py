class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        d = [0] * len(nums)
        d[0] = nums[0]
        safe, d[1] = [False, nums[1]] if nums[1] > nums[0] else [True, d[0]]
        
        for idx in range(2, len(nums)):
            # print(d)
            d[idx] = d[idx - 2] + nums[idx]
            if d[idx - 1] >= d[idx]: # Not robbing the curr house == current best value
                d[idx] = d[idx - 1]
                safe = True
            else: 
                # Robbing the current house with two possibilities. 
                # 1: The best value up to the one before the previous house + current, (i.e. d[idx -2] + val)
                # 2: The best value up to the previous house (i.e. d[idx - 1] + val), but this is only possible if we did not rob the previous house
                # But either way we are robbing the current house, hence set safe = False
                if safe and d[idx - 1] + nums[idx] > d[idx]:
                    d[idx] = d[idx - 1] + nums[idx]
                safe = False
                
        return d[-1]
        