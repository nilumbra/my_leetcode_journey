from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def build_graph(edges):
            graph = defaultdict(list)
            for (tail, head) in edges:
                graph[tail].append(head)
            return graph
        
        def dfs(i):
            if i in G:
                # For loop terminates when having visited all descendent of node i 
                for child in G[i]: 
                    dfs(child)
                    if child in parentSet:
                        parentSet.remove(child)
                        parentSet.add(i)

                del[G[i]] # Vistied all descendents. Color the i-node black
                parentSet.add(i)
        
        G = build_graph(edges)
        parentSet = set()
        for node in range(n):                
            dfs(node)
            
        
        return list(parentSet)

                
                
        