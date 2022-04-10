class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2: return n
        
        d, dd = 1, 2
        curr = 0
        for i in range(3, n + 1):
            curr = d + dd 
            d = dd 
            dd = curr
        
        return curr
            
        