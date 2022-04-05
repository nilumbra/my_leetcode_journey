class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        
        parent = [ -1 for i in range(n)]
        def find(a):
            if parent[a]<0:
                return a
            parent[a] = find(parent[a])
            return parent[a]

        def Union(a,b):
            parent[a] += parent[b]
            parent[b] = a

        ans = n-1
        for i,j in connections:
            a = find(i)
            b = find(j)
            if a!=b:
                Union(a,b)
                ans-=1
        return ans