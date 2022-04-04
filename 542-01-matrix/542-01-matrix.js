/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var updateMatrix = function(mat) {
    var m = mat.length, 
        n = mat[0].length,
        d = [...Array(m)].map(row=>Array(n).fill(-1));
    
    /**
     * @ param {number} i 
     * @ param {number} j
     * @ return {Iterable}
    */
    function* getValidNeighbors(i, j) {
       var dir4 = [[-1, 0], [0, 1], [1, 0], [0, -1]],
          x = 0;

       while (x < 4) {
          const row = i + dir4[x][0],
                col = j + dir4[x][1];
          if (0 <= row && row < m && 0 <= col && col < n) {
             // console.log(0<= row < m, 0 <= col < n)
             yield [row, col]   
          }
          x++;
       }
    }
    
    
   this_layer = [];
   next_layer = [];
   level = 1;
   // initialize d: number[][]
   for (let i = 0; i < m ; i++) {
      for (let j = 0; j < n; j++){
         if (mat[i][j] == 0) {
            d[i][j] = 0; 
            this_layer.push([i, j])
         } 
      }
   }

   while (this_layer[0]) {
      // Process this_layer
      // console.log(this_layer)
      for (const this_cell of this_layer) {
         for (const [r,c] of getValidNeighbors(...this_cell)) {
            if(d[r][c] == -1) {
               d[r][c] = level;
               next_layer.push([r, c])
            }
         }   
      }

      level++;
      this_layer = next_layer;
      next_layer = []
   }

   return d
};