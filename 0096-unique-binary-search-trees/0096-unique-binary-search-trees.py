class Solution:
    def numTrees(self, n: int) -> int:
      memo = {0 : 1, 1: 2}
      def f(s:int, e: int) -> int:
        nonlocal memo
        if e - s in memo:
          return memo[e-s]

        us = 0
        for r in range(s+1, e):
          us += f(s, r-1) * f(r+1, e)

        memo[e-s] = us + f(s+1, e) + f(s, e-1)
        return memo[e-s]
      
      return f(1, n)
        
      
      