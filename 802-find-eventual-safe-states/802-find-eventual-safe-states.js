/**
 * @param {number[][]} graph
 * @return {number[]}
 */
var eventualSafeNodes = function(graph) {
    const GRAY = 1,
          BLACK = 2,
          color = {};
          
    
    function dfs(node) {
        // console.log(color)
        if (!color[node]) {
            // console.log(`dfs(${node})`)
            color[node] = GRAY;
            for (const child of graph[node]) {
                if (color[child] == BLACK) continue
                if (color[child] == GRAY || !dfs(child)) return false
            }

            color[node] = BLACK
            return true
        } else {
            return color[node] == BLACK
        }
        
    }
    
    return Array.from({length: graph.length}, (_, i) => i).filter(dfs)
};