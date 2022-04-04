/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function(graph) {
    if (graph[0].length == 0 ) return []

    const visited = {}, 
            ans = [],
          stack = [];

    stack.push(0)

    while (stack.length != 0) {
        
        var cur = stack.at(-1);

        if (!visited.hasOwnProperty(cur)) {
            visited[cur] = 0;
        } else {
            visited[cur]++;
        }

        if (!graph[cur][visited[cur]] ) { // the cur node does not have an outgoing edges at all && has visited all outcoming edes from the cur_node 
            if (cur == graph.length - 1) {
                // console.log(stack)
                ans.push(Array.from(stack))
                // console.log(ans)
            }
            // console.log(visited)
            delete visited[cur]
            stack.pop()
        } else {
            var next_node = graph[cur][visited[cur]];
            stack.push(next_node)
        }
        
        // console.log(stack)
    }

    return ans
}