import heapq
import bisect
class Solution(object):
    def kWeakestRows(self, mat, k): 
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        h = []
        l = len(mat[0])
        for (idx, row) in enumerate(mat):  # m * log(nk) ==> the upperbound
            ones = l - bisect.bisect_left(row[::-1], 1) # log(n)
            heapq.heappush(h, (ones, idx)) # log(k)
        
        ans = []
        for i in range(k): # O(k * log(k))
            ans.append(heapq.heappop(h)[1])
        
        return ans
            
    