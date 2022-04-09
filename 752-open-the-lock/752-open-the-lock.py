from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                for _ in {-1, 1}:
                    d = (int(node[i]) + _) % 10
                    yield node[:i] + str(d) + node[i+1:]
        
        deadends = set(deadends)
        Q = deque()
        Q.append(('0000', 0))
        seen = {'0000'}
        
        while Q:
            node, depth = Q.popleft()
            if node == target: return depth
            if node in deadends: continue
            for nei in neighbors(node):
                if nei not in seen:
                    Q.append((nei, depth + 1))
                    seen.add(nei)
        
        return -1
                