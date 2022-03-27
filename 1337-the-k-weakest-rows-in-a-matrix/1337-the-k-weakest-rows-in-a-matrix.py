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
        for (idx, row) in enumerate(mat):
            ones = l - bisect.bisect_left(row[::-1], 1)
            heapq.heappush(h, (ones, idx))
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(h)[1])
        
        return ans
            