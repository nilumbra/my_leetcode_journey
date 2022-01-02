/**
 * @param {number[][]} times
 * @param {number} n
 * @param {number} k
 * @return {number}
 */



// times = [[2,1,1],[2,3,1],[3,4,1]], n = 4
// adj = buildAdjList(times, n)
// adj <-- [[], 
//          [{head: 1, w: 1}, {heada: 3, w: 1}],
//          [{head:4, w:1}], 
//          []]
function buildAdjList(times, n){
    let adj = Array.from(Array(n), ()=>new Array());
    times.forEach((de) => {
        // adj[0] <- node1 
        adj[de[0] - 1].push({head: de[1], w: de[2]})
    })
    return adj
}


// inputs: 
//  k:= source (use k-1 to access adj)
// adj:= G(V, E), w: E--> Realnumber
function dijkstra(k, adj){
    var delta = Array.from(Array(adj.length), x => x= Infinity) // initialize estimated distance from source;
    
    delta[k - 1] = 0; // initialize source 
    const Q = new Set();
    for (key in [...Array(adj.length).keys()]){
        Q.add(parseInt(key))
    }
    // var S = []; 
    while(!_isEmpty(Q)){
        minNode = _extractMin(Q, delta);

        // Relax all edges from the minNode 
        for(let target of adj[minNode]){
            _relax(delta, minNode, target)    
        }
    }
    return delta
}

function _relax(delta, minNode, target){
    // Only target.head needs '-1', because the nodes defined in input start from 1
    if(delta[target.head - 1] > delta[minNode] + target.w){
        delta[target.head - 1] = delta[minNode] + target.w;
    }
}

function _isEmpty(set){
    return set.size === 0;
}

// O(n) to extractMin 
function _extractMin(Q, dist){
    var minD = Infinity,
        minNode = null;
    for (let node of Q){
        if(dist[node] <= minD) {
            minD = dist[node];
            minNode = node;
        }
    }
    
    Q.delete(minNode)
    return minNode
}


// 
times = [[2,1,1],[2,3,1],[3,4,1]], 
    n = 4, k = 2;
// times = [[1,2,1]], n = 2, k = 2

var networkDelayTime = function(times, n, k) {
    let adj = buildAdjList(times, n);
    let  distances = dijkstra(k, adj),
        longest_delay = -1;

    for (let d of distances){
        if(d >= longest_delay) longest_delay = d;
        if(d == Infinity) return -1
    }
    return longest_delay
};

console.log(networkDelayTime(times, n, k))