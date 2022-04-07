/**
 * @param {number} n
 * @param {number} headID
 * @param {number[]} manager
 * @param {number[]} informTime
 * @return {number}
 */
var numOfMinutes = function(n, headID, manager, informTime) {
    const graph = {};
    
    // build a graph in hashmap form from manager array
    function build_graph(manager) {
        for ([idx, parent] of manager.entries()) {
            if (parent == -1) {
                continue
            }    
            
            if (!graph[parent]){
                graph[parent] = [idx];
            } else {
                graph[parent].push(idx)
            }
        }
    }
    
    build_graph(manager)

    const seen = new Set();
    function dfs(node, time) {
        if (!graph[node]) return 0
        
        var maxTime = time;
        for (const child of graph[node]) {
            // console.log(`dfs(${child}, ${informTime[child]})`)
            let descentdentInformTime = dfs(child, informTime[child]);
            maxTime = Math.max(descentdentInformTime + time, maxTime);
        }
        
        // console.log(`Inform time at node:${node} is ${maxTime}`)
        return maxTime
    }

    return dfs(headID, informTime[headID])
};