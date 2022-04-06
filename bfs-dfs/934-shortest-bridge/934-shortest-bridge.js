/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestBridge = function(grid) {
    // Use dfs to find two islands 
    // Then do bfs starting from every cell of one of the island
    const size = grid.length;
    
    const island1 = new Set(),
          island2 = new Set();
    
    function* validNeighbors(i, j){
        for ([x, y] of [[0, -1], [-1, 0], [0, 1], [1, 0]]) {
            const r = i + x,
                  c = j + y;
            if (r < 0 || r >= size || c < 0 || c >= size) {
                continue
            }       
            yield [r, c]
        }
    }
    
    function dfs(i, j, island){
        island.add(JSON.stringify([i, j]))
        for (this_cell of validNeighbors(i, j)) {
            if (grid[this_cell[0]][this_cell[1]] == 1 && !island.has(JSON.stringify(this_cell))){
                dfs(...this_cell, island)
            }
        }
    }
    
    /**
     * @param {number[]} island1
     * @param {Set<string>} island2
     * @return {number}
     */
    function bfs_shortest_path(island1, island2) {
        var this_level = [],
            next_level = [],
            frontier  = [],
            level = 0;
        
        this_level = island1
        
        while (this_level.length != 0) {
            for (const this_cell of this_level) {
                for (const [r, c] of validNeighbors(...this_cell)) {
                    if(island2.has(JSON.stringify([r, c]))) return level
                    if(grid[r][c] == 0) {
                        grid[r][c] = 1
                        next_level.push([r, c])
                    }
                }
            }
            
            this_level = next_level;
            next_level = [];
            level++;
        }
        return level
    }
  
    var flag = 1
    for (let i = 0;i < size ; i++) {
        for (let j = 0; j < size; j++){
            if(grid[i][j] == 1 && !island1.has(JSON.stringify([i, j])) && !island2.has(JSON.stringify([i, j]))){
                // console.log(i, j)
                if (flag == 2){
                    dfs(i, j, island2)    
                    // console.log(island2)
                    // console.log(grid)
                }
                
                if (flag == 1) {
                    dfs(i, j, island1)
                    // console.log(island1)
                    // console.log(grid)
                    flag = 2;
                }
            }
        }
    }
    
    // console.log(island1)
    // console.log(island2)
    
    island1_array = Array.from(island1).map(e => JSON.parse(e));
        
    return bfs_shortest_path(island1_array, island2)
};