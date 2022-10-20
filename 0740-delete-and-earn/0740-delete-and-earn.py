class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        v_c = defaultdict(int);
        nums.sort()
        # since Python 3.6, the dict key's order is guarenteed to be insertion order
        for num in nums:
            v_c[num] += num
        
        _k = -1
        _s = s = 0
        #print(v_c)
        for k in v_c.keys():
            if k - _k != 1:
                _s, s = s, s + v_c[k]
            else: 
                _s, s = s, max(s, _s + v_c[k])
            _k = k    
        return s