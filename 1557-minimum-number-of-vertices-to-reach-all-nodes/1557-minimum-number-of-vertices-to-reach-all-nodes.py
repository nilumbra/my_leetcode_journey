from collections import defaultdict
class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        parent = {}
        for tail, head in edges:
            parent[head] = tail
        
        nonreachable = []
        for i in range(n):
            if i not in parent: 
                nonreachable.append(i)
                
        return nonreachable
            
        