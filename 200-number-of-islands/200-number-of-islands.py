class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        w, h = len(grid[0]), len(grid)

        def recurse(pos):
            """
            Given an index within bounds of grid, recursively explore all reachable indices and mark them as explored. 
            """   
            visited.add(pos)
            i, j = pos[0], pos[1]

            if i + 1 < h and grid[i+1][j] == "1" and (i + 1, j) not in visited :
                recurse((i+1, j))

            if i - 1 >= 0 and grid[i-1][j] == "1" and (i - 1, j) not in visited:
                recurse((i-1, j))

            if j + 1 < w and grid[i][j+1] == "1" and (i, j + 1) not in visited:
                recurse((i, j + 1))

            if j - 1 >= 0 and grid[i][j-1] == "1" and (i, j - 1) not in visited:
                recurse((i, j - 1))
            
            return

        count = 0
        for i in range(h):
            for j in range(w):
                if (i, j) not in visited and grid[i][j] == "1":
                    recurse((i, j))
                    count += 1
                    # print(visited)
                
                
        return count
    
    