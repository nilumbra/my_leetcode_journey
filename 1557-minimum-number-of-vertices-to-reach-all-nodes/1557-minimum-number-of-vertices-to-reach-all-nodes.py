class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        unreachable_nodes = set(list(range(n)))
        for tail, head in edges:
            if head in unreachable_nodes:
                unreachable_nodes.remove(head)    
        
        return list(unreachable_nodes)
            
        