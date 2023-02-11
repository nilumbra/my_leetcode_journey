class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        def bt(com, rest, k):
          if k == 0:
            ans.append(com) 
          else:
            for i, x in enumerate(rest):
              bt(com+[x], rest[i+1:], k - 1)
          
        bt([], list(range(1, n+1)), k)
        return ans
            
            