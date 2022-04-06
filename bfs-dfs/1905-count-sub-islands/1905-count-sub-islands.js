/**
 * @param {number[][]} grid1
 * @param {number[][]} grid2
 * @return {number}
 */
var countSubIslands = function(grid1, grid2) {
    /*
        Find an island in grid2 as usual
        But do check to see at each recursive step if the island discovered so far
        is a sub-island. 
        Return false when the island is no longer a sub-island
    */
    var visited = new Set(),
              w = grid2[0].length,
              h = grid2.length,
          number = 0;
            
    var move = function(i, j) {
    // Recursively takes a valid 4-directional move
    // Returns true if the recursion chain finds a sub-island
        var is_subisland = grid1[i][j] == 1;
        visited.add([i,j].toString())
        
        if (i - 1 >= 0 && grid2[i - 1][j] == 1 && !visited.has([i - 1,j].toString())) {
            // Notice since we want move() to check off all cells in an island to visited even if its is not a valid sub-island cell,
            // we can't let move() be shortcircuite by a failed sub-island cell check 
            is_subisland = move(i - 1, j) && is_subisland;
        }
        
        if (i + 1 < h && grid2[i + 1][j] == 1 && !visited.has([i + 1, j].toString())) {
            is_subisland = move(i + 1, j) && is_subisland;
        }
        
        if (j - 1 >= 0 && grid2[i][j - 1] == 1 && !visited.has([i, j - 1].toString())) {
            is_subisland = move(i, j - 1) && is_subisland;
        }
        
        if (j + 1 < w && grid2[i][j + 1] == 1 && !visited.has([i, j + 1].toString())) {
            is_subisland = move(i, j + 1) && is_subisland;
        }
        
        // console.log(i, j, is_subisland)
        // The recursion terminates whenever the current (i,j) is already visited or out of bounds
        return is_subisland
    }
    
    
    for (let i = 0;i < h;i++) {
        for (let j = 0;j < w;j++){
            if (grid2[i][j] == 1 && !visited.has([i,j].toString()) && move(i, j)) {
                number++;
                // console.log(`----${number}----`)
            }
        }
    }
    
    return number
};