/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function(isConnected) {
    var provinces = 0,
        seen = new Set(),
        len = isConnected.length;

    function dfs(i, isConnected){
        seen.add(i)        
        // console.log(isConnected[i])
        for (const [idx, othernode] of isConnected[i].entries()) {
            if (idx == i) continue
            if (othernode && !seen.has(idx)) {
                dfs(idx, isConnected)
            }
        }
    }
    
    
    for (let idx = 0; idx < len; idx++) {
        if(!seen.has(idx)) {
            // console.log(`dfs(${idx}, ${isConnected[idx]})`)
            dfs(idx, isConnected)
            provinces++;
        }
    }
    
    return provinces
};