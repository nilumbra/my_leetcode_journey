/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function(heights) {
    // Empty input
    if (!heights || !heights[0]) return []
    
    const w = heights[0].length,
          h = heights.length;
    
    // Reachable set
    const pacific_reachable = new Set(),
          atlantic_reachable = new Set();
    
    // dfs to add cells to two ocean-reachable set
    // The function should be invoked with oceanside cells' index
    function dfs(i, j, reachable) {
        reachable.add(JSON.stringify([i, j]))
        // console.log(reachable)
        for (let [x, y] of [[-1, 0], [0, -1], [1, 0], [0, 1]]) {
            const r = i + x, 
                  c = j + y;
            // console.log(r, c)
            if (reachable.has(JSON.stringify([r, c]))) continue
            if (r < 0 || r >= h || c < 0 || c >= w) continue
            
            if (heights[r][c] >= heights[i][j]) {
                dfs(r, c, reachable)
            }
        }
    }
    
    for (let i = 0; i < w; i++) {
        dfs(0 ,i, pacific_reachable)
        dfs(h - 1, i, atlantic_reachable)
    }
    
    for (let i = 0; i < h; i++) {
        dfs(i, 0, pacific_reachable)
        dfs(i, w - 1, atlantic_reachable)
    }
    //console.log(Array.from(pacific_reachable.forEach(coor=>JSON.parse(coor))))
    const intersection = Array.from(pacific_reachable).filter(x => atlantic_reachable.has(x));
    intersection.forEach((e, i, arr) => { arr[i] = JSON.parse(e)});
    // console.log(intersection)

    
    // Do intersection and parse every coor into real array. Since they were stringified.
    return intersection
};

