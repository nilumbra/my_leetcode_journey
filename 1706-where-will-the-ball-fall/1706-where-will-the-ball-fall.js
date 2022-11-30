/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findBall = function(grid) {
    // starts from the last row
  var res = [...Array(grid[0].length).keys()]

  for (let i = grid.length - 1; i >= 0; i--) {
    let temp = []
    for (let j = 0; j < res.length; j++) {
      
       let i_look_at = j + grid[i][j]
       if ((i_look_at >= 0) && (i_look_at < grid[0].length) 
           && (grid[i][j] === grid[i][i_look_at])) {
          temp.push(res[i_look_at])
       } else {
         temp.push(-1)
       }
      
    }
    res = temp
  }
  return res
};