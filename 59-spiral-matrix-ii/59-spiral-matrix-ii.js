const states = ["right", "down", "left", "up",];
const moves = {"right": [0, 1], "down": [1, 0], "left": [0, -1], "up": [-1, 0],};


/**
 * @param {number} n
 * @return {number[][]}
 */
function generateMatrix(n) {
  // Initialize matrix
  const matrix = new Array(n).fill(0).map(() => new Array(n).fill(0));

  // Initialize state
  var curr_state = 0;
  var curr_pos = [0, 0];

  function isGoingToChangeDir() {
    const [_x, _y] = nextPos(...curr_pos, ...moves[states[curr_state]]);

    return _x < 0 ||  _x > n - 1 || _y < 0 || _y > n - 1 || matrix[_x][_y] > 0; // Need to change dir if next position out of bounds or next position has been filled
  }

  for (let num = 1; num <= n * n; num++) {

    matrix[curr_pos[0]][curr_pos[1]] = num;
    if (isGoingToChangeDir()) {
      //change direction
      curr_state  = (curr_state + 1) % 4;
      curr_pos = nextPos(...curr_pos, ...moves[states[curr_state]]);
    } else {
      // Do not change state and use it to get next position;
      curr_pos = nextPos(...curr_pos, ...moves[states[curr_state]]);
    }
    // log(states[curr_state]);
    // log(num)
    // log(matrix);
    // log('--------------------')
  }
    
  return matrix;
}

/**
 * @returns {number[]} updated pos 
 */
function nextPos(x, y, dx, dy) {
  return [x + dx, y + dy];
}



