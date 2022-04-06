class MaxAreaOfIsland(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #
        m = len(grid)
        n = len(grid[0])
        mArea = 0;
        count = 0

        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    mArea = max(mArea, self.bfs(grid, i, j))
                    # print(mArea)
        return mArea
        
    # Explore the island and return its area
    def bfs(self, grid, r, c):
        area = 0
        frontier = [(r,c)]
        visitedNeighbor = {(r,c)}

        while(bool(frontier)):
            nextNeighbors = []
            for e in frontier:
                area += 1
                self.grabNeighbers(grid, e, nextNeighbors, visitedNeighbor)
                # print(nextNeighbors)

            frontier = nextNeighbors
            # print(nextNeighbors)
        # print(visitedNeighbor)
        for coor in visitedNeighbor:
            grid[coor[0]][coor[1]] = 0
        # print(area)
        return area 
    
    # area = # of neighbers you grab + 1
    def grabNeighbers(self, grid, coor, neighborList, visitedNeighbor):
        # print(coor)
        # print(grid[coor[0]][coor[1]])

        # check top
        if(coor[0] >= 1 and grid[coor[0] - 1][coor[1]] == 1 and (coor[0] - 1, coor[1]) not in visitedNeighbor): 
            print("check top if called")
            neighborList.append((coor[0]-1, coor[1]))
            visitedNeighbor.add((coor[0]-1, coor[1]))
        
        # check bottom
        if(coor[0] < len(grid) - 1 and grid[coor[0] + 1][coor[1]] == 1 and (coor[0] + 1, coor[1]) not in visitedNeighbor): 
            print("check bottom if called")
            neighborList.append((coor[0]+1, coor[1]))
            visitedNeighbor.add((coor[0]+1, coor[1]))
            
        #check left 
        if(coor[1] >= 1 and grid[coor[0]][coor[1] - 1] == 1 and (coor[0], coor[1] - 1) not in visitedNeighbor):
            print("check left if called") 
            neighborList.append((coor[0], coor[1] - 1))
            visitedNeighbor.add((coor[0], coor[1] - 1))
        
        #check right 
        if(coor[1] < len(grid[0]) - 1 and grid[coor[0]][coor[1] + 1] == 1 and (coor[0], coor[1] + 1) not in visitedNeighbor): 
            print("check right if called")
            neighborList.append((coor[0], coor[1] + 1))
            visitedNeighbor.add((coor[0], coor[1] + 1))

def Test_grabNeighers(grid, r, c, visitedNeighbor):
    neighborList = []
    solver = MaxAreaOfIsland()
    solver.grabNeighbers(grid, (r, c), neighborList, visitedNeighbor)

    return neighborList

def Test_bfs(grid, r, c):
    neighborList = []
    solver = MaxAreaOfIsland()

    area = 0
    frontier = [(r,c)]
    visitedNeighbor = {(r,c)}

    while(bool(frontier)):
        nextNeighbors = []
        for e in frontier:
            area += 1
            solver.grabNeighbers(grid, e, nextNeighbors, visitedNeighbor)
            # print(nextNeighbors)

        frontier = nextNeighbors
        # print(nextNeighbors)
    # print(visitedNeighbor)
    for coor in visitedNeighbor:
        grid[coor[0]][coor[1]] = 0
    # print(area)
    return area 

if __name__ == '__main__':
    solver = MaxAreaOfIsland()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

    visitedNeighbor = set()
    # print(Test_grabNeighers(grid, 6, 8, visitedNeighbor))
    # print(Test_bfs(grid, 0, 7))
    print(solver.maxAreaOfIsland(grid))