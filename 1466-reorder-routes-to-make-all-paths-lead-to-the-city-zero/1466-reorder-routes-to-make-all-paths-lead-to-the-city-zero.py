from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        def build_undirected_graph(connections: List[List[int]]) -> dict:
            udgraph = {}
            for tail, head in connections:
                if tail not in udgraph:
                    udgraph[tail] = [-head]
                else:
                    udgraph[tail].append(-head)
                    
                if head not in udgraph:
                    udgraph[head] = [tail]
                else:
                    udgraph[head].append(tail)
            
            return udgraph
            
        G = build_undirected_graph(connections)
        frontier = deque()
        frontier.append(0)
        count = 0
        while frontier:
            curr_city = frontier.popleft()
            # print(curr_city)
            for nei in G[curr_city]:
                if abs(nei) in G: # nei is not discovered yet
                    frontier.append(abs(nei))
                    if nei < 0: count += 1
            del G[curr_city]
        
        return count
        