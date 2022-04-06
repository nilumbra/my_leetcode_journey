class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        w, h = len(grid[0]), len(grid)
        visited = set()
        
        def move(i, j):
            """
            Recursively takes a move from the given (i, j) until all connected cells are visited
            Returns whether the connected land cells consist an enclave
            """
            nonlocal visited
            nonlocal count
            res = True
            
            if i * j == 0 or i == h - 1 or j == w - 1:
                res = False

            visited.add((i, j)) # Once a pos is discovered, no more messing around
            # print(count)
            count += 1
            
            if (i - 1 >= 0 and grid[i-1][j] == 1 and (i - 1, j) not in visited):
                res = move(i - 1, j) and res
            if (i + 1 < h and grid[i+1][j] == 1 and (i + 1, j) not in visited):
                res = move(i + 1, j) and res
            if (j - 1 >= 0 and grid[i][j-1] == 1 and (i, j - 1) not in visited):
                res = move(i, j - 1) and res
            if (j + 1 < w and grid[i][j+1] == 1 and (i, j + 1) not in visited):
                res = move(i, j + 1) and res
                       
                    
            # print(i, j, res, count)
            return res
        
        s = 0 
        for i in range(h):
            for j in range(w):
                count = 0
                if (grid[i][j] == 1 and (i, j) not in visited and move(i, j)):
                    s += count
                    # print(s)
                    # print(count)
        
        return s
                    