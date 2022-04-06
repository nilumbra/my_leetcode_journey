class Solution(object):
    def maxAreaOfIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        mArea = 0;
        count = 0

        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    mArea = max(mArea, self.bfs(grid, i, j))
        return mArea
        
    def bfs(self, grid, r, c):
        area = 0
        frontier = [(r,c)]
        visitedNeighbor = {(r,c)}

        while(bool(frontier)):
            nextNeighbors = []
            for e in frontier:
                area += 1
                self.grabNeighbors(grid, e, nextNeighbors, visitedNeighbor)

            frontier = nextNeighbors
        for coor in visitedNeighbor:
            grid[coor[0]][coor[1]] = 0
        return area 
    
    def grabNeighbors(self, grid, coor, neighborList, visitedNeighbor):

        if(coor[0] >= 1 and grid[coor[0] - 1][coor[1]] == 1 and (coor[0] - 1, coor[1]) not in visitedNeighbor): 
            neighborList.append((coor[0]-1, coor[1]))
            visitedNeighbor.add((coor[0]-1, coor[1]))
        
        if(coor[0] < len(grid) - 1 and grid[coor[0] + 1][coor[1]] == 1 and (coor[0] + 1, coor[1]) not in visitedNeighbor): 
            neighborList.append((coor[0]+1, coor[1]))
            visitedNeighbor.add((coor[0]+1, coor[1]))
            
        if(coor[1] >= 1 and grid[coor[0]][coor[1] - 1] == 1 and (coor[0], coor[1] - 1) not in visitedNeighbor):
            neighborList.append((coor[0], coor[1] - 1))
            visitedNeighbor.add((coor[0], coor[1] - 1))
        
        if(coor[1] < len(grid[0]) - 1 and grid[coor[0]][coor[1] + 1] == 1 and (coor[0], coor[1] + 1) not in visitedNeighbor): 
            neighborList.append((coor[0], coor[1] + 1))
            visitedNeighbor.add((coor[0], coor[1] + 1))