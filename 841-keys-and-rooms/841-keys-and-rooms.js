/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function(rooms) {
    var queue = [],
         seen = new Set(),
         head = 0,
         curr = null;
          
    queue.push(0)
    seen.add(0)
    
    while (queue.length !== head) {
        curr = queue[head];
        for (const key of rooms[curr]) {
            if (!seen.has(key)) {
                queue.push(key)
                seen.add(key)
            }
        }
        head++;
    }
    
    
    return seen.size === rooms.length
};