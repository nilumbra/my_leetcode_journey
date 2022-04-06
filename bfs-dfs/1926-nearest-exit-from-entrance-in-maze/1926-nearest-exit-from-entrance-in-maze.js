/**
 * @param {character[][]} maze
 * @param {number[]} entrance
 * @return {number}
 */
var nearestExit = function(maze, entrance) {
    const w = maze[0].length,
          h = maze.length;
    
    function* valid_neighbors(i, j){
        for (const [x, y] of [[0, -1], [-1, 0], [0, 1], [1, 0]]) {
            const r = i + x, 
                  c = j + y;
            if (0 <= r && r < h && 0 <= c && c < w) {
                yield [r, c]
            }
        }
    }
    
    function getAllExits(maze, ex, ey){
        const exits = new Set();
        
        //four corners
        for (const [i, j] of [[0, 0], [0, w - 1], [h - 1, w - 1], [h - 1, 0]]){
            if(!(ex === i && ey === j) && maze[i][j] === '.'){
                exits.add(JSON.stringify([i, j]))
            }
        }
        
        // left side and righ side
        for(let i = 1; i < h - 1; i++){
            if(!(ex === i && ey === 0) && maze[i][0] === '.') {
                exits.add(JSON.stringify([i, 0]))
            }
            
            if(!(ex === i && ey === w - 1) && maze[i][w - 1] === '.') {
                exits.add(JSON.stringify([i, w - 1]))
            }
        }
        
        // top and bottom
        for(let i = 1; i < w - 1; i++){
            if(!(ex === 0 && ey === i) && maze[0][i] === '.') {
                exits.add(JSON.stringify([0, i]))
            }   
            if(!(ex === h - 1 && ey === i) && maze[h - 1][i] === '.') {
                exits.add(JSON.stringify([h - 1, i]))
            }
        }
        return exits
    }
    
    
    // Given [i, j], find the length of the shortest path to entrance
    // Return Infinity if no such path exist between [i, j] and entrance
    function find_shortest_path(i, j, goals){
        // entrance cannot be exit
        var this_level = [[i, j]],
              next_level = [],
              visited = new Set(),
                level = 1;

        visited.add(JSON.stringify([i, j]))
        
        // if(level === 0 && i === entrance[0] && j === entrance[1]) return Infinity;
        
        while (this_level.length !== 0) {
            for (const this_cell of this_level) {
                // console.log(this_level)
                for (const [r, c] of valid_neighbors(...this_cell)) {
                    // console.log(this_cell, goals)
                    if (goals.has(JSON.stringify([r, c]))){
                        // console.log(this_cell)
                        return level
                    }

                    if (maze[r][c] === '.' && !visited.has(JSON.stringify([r, c]))) {
                        // console.log(this_cell, visited)
                        next_level.push([r, c])
                        visited.add(JSON.stringify([r, c]))
                    }
                }    
            }
            
            level++;
            this_level = next_level;
            next_level = [];
        }
        
        return -1
    }
    
    const pathlens = [],
          goals = getAllExits(maze, ...entrance);
    
    // console.log(goals)
    
    
    return find_shortest_path(...entrance, goals);
    
};