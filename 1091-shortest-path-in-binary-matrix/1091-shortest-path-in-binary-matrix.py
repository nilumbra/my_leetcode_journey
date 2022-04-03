from collections import deque 
import itertools
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        w, h = len(grid[0]), len(grid)
        dir_8 = lambda i, j: [(i + x, j + y) for x, y in itertools.product([-1, 0, 1], repeat=2) if not (x == 0 and y == 0)]
        
        if grid[0][0] == 1 or grid[w - 1][h - 1] == 1: return -1
        if len(grid) == 1 and grid[0][0] == 0: return 1
        
        def get_valid_neighbors(i, j):
            # print("neighbors:", [(x, y) for x, y in dir_8(i, j) if 0 <= x < h and 0 <= y < w and grid[x][y] == 0])
            return [(x, y) for x, y in dir_8(i, j) if 0 <= x < h and 0 <= y < w and grid[x][y] == 0]
    
        
        
        
        frontier = deque() # cells that have been discovered but not visited
        discovered = set()
        
        level = 1
        frontier.append((level, (0, 0)))
        discovered.add((0, 0))
        
        while frontier:
            level, this_cell = frontier.popleft() # visit this cell
            # print(this_cell, discovered)
            for cell in get_valid_neighbors(*this_cell): # discovering new adjacent cells
                if cell not in discovered:
                    frontier.append((level + 1, (cell[0], cell[1])))
                    discovered.add(cell)
                if cell == (w - 1, h - 1):
                    return level + 1
                    
            
        
        return -1 # BFS ended, but no bottom-right cell is no reached; hence no clear path
                    
        
        
    
        
        
            