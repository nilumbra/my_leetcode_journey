from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        def build_graph(redEdges, blueEdges):
            graph = defaultdict(list)
            for t, h in redEdges:
                graph[t].append((h, "red"))
            
            for t, h in blueEdges:
                graph[t].append((h, "blue"))
                
            return graph
        
        graph = build_graph(redEdges, blueEdges)
        
        seen = set()
        frontier = deque()
        answer = [-1] * n 
        
        
        seen.add((0, 0, None)) # (tail, head, color)
        answer[0] = 0
        level = 1
        for node in graph[0]: # Add nodes adjacent to 0 to frontier, answer, and seen
            frontier.append(node + (level, ))
            seen.add((0, node[0], node[1]))
            if answer[node[0]] == -1: 
                answer[node[0]] = 1
          
        # print(answer)
        # print(frontier)
        # assert frontier.index(0) == (1, 1, 1)
        
        while frontier: # all frontier nodes are seen
            i, c, l = frontier.popleft() # current level
            # print(frontier)
            # print(seen)
            for _i, _c in graph[i]: # next level
                if (i, _i, _c) not in seen:
                    # print(_i, _c)
                    if _c != c:  # if alternating color && the neighboring node has unexplored edges
                        frontier.append((_i, _c, l + 1))
                        if answer[_i] == -1:
                            answer[_i] = l + 1
                        seen.add((i, _i, _c))
        
        return answer
                    
                    
            
            
            
        
        
        