function closedIsland(grid: number[][]): number {
    // Observation 1: 
    // If piece (i, j) satisfies i * j == 0 or i == grid.length - 1 or j == grid[0].length - 1, then the island containing the piece is not closed. (i.e. ok to discard)
    const w: number = grid[0].length,
          h: number = grid.length;

    type Pos = [
        i: number,
        j: number
    ];
    
    const visited: Set<string> = new Set();
    
    function findIsland(pos: Pos): boolean {
        // Assumes grid at pos is a 0, DFS from that position to find the closed island.   
        // Returns true only if every possible path has been traversed from pos and
        // did not encounter any edge in the process
        let i: number = pos[0],
            j: number = pos[1];
        
        var res: boolean = true;
        visited.add(pos.toString()) // Vistied 0 should not be visited again. While 
        // DFS recursive call ends without encountering any edge
        if ((i * j == 0) || (i == h - 1) || (j == w - 1)) {
            res = false;
        }
        
//         var explorable: number[][] = []
//         if((i+1) < h && grid[i+1][j] == 0 && !visited.has([i+1, j].toString())){
//             explorable.push([i+1, j])
//         }
        
//         if((i-1) >= 0 && grid[i-1][j] == 0 && !visited.has([i-1, j].toString())){
//             explorable.push([i-1, j])
//         }
        
//         if ((j+1) < w && grid[i][j+1] == 0 && !visited.has([i, j+1].toString())){
//             // console.log("right")
//             explorable.push([i, j+1])
//         }
        
//         if ((j-1) >= 0 && grid[i][j-1] == 0 && !visited.has([i, j-1].toString())){
//             // console.log("left")
//             explorable.push([i, j-1])
//         }
        
//         var visited_values = ""
//         for(const k of visited.values() ){
//             visited_values += k + ", "  
//         }
        // console.log(`At :${pos} Next explorable: ${explorable}`)
        // console.log(`visited currently contains ${visited_values}`)
//         if([i+1,j].toString() == '1,9'){
//     console.log((i+1) < h && grid[i+1][j] == 0 && !visited.has([i+1, j].toString()))
// }
        
        if ((i+1) < h && grid[i+1][j] == 0 && !visited.has([i+1, j].toString())){
            // console.log("down")
            res = findIsland([i+1, j]) && res;
        }
        if ((i-1) >= 0 && grid[i-1][j] == 0 && !visited.has([i-1, j].toString())){
            // console.log("up")
            res = findIsland([i-1, j]) && res;
        }
        if ((j+1) < w && grid[i][j+1] == 0 && !visited.has([i, j+1].toString())){
            // console.log("right")
            res = findIsland([i, j+1]) && res;
        }
        if ((j-1) >= 0 && grid[i][j-1] == 0 && !visited.has([i, j-1].toString())){
            // console.log("left")
            res = findIsland([i, j-1]) && res;
        }

        return res
    }
    

    let count: number = 0;
    for (let i: number = 0; i < h; i++) {
        for (let j: number = 0; j < w; j++) {
            if (grid[i][j] == 0 && !visited.has([i, j].toString()) && findIsland([i, j])) {count++;}
        }
    }

    return count
};
