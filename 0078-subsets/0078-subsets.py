class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def select(nums, maskN):
            #print(f'select {bin(maskN)[2:]}')
            res = []
            i = len(nums) - 1
            while maskN:
                if maskN & 1:
                    res.append(nums[i])
                maskN >>= 1
                i -= 1
            assert maskN == 0 
            return res
                
        
        Pn = 2 ** len(nums)
        ans = []
        for i in range(Pn):
            ans.append(select(nums, i))
        
        return ans
   