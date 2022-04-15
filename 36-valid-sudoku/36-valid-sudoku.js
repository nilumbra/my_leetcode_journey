function isValidSudoku(board: string[][]): boolean {
    var validityMod: Set<string> = new Set();
    
    // Check rows
    for (const row of board) {
        for (const cell of row) {
            if (cell != ".") {
                if(!validityMod.has(cell)) {
                    validityMod.add(cell)
                } else {
                    return false
                }
            }
        }
        validityMod = new Set();
    }
    
    // Check columns
    for(let j = 0; j < 9; j++) {
        for (let i = 0; i < 9; i++) {
            const cell: string = board[i][j]
            if (cell != ".") {
                if (!validityMod.has(cell)) {
                    validityMod.add(cell)
                } else {
                    return false
                }
            }
        }
        validityMod = new Set();
    }
    
    function* getSubBox(n: number) {
        const q: number = Math.floor(n / 3),
              r: number = n % 3;
        
        const startY: number = q * 3,
              startX: number = r * 3,
              endY: number   = q * 3 + 2,
              endX: number   = r * 3 + 2;
        
        for (let i = startX; i <= endX; i++) { 
            for (let j = startY; j <= endY; j++) {
                yield [j, i]
            }
        }
    }
    
    // Check sub-boxes
    for (let n = 0; n < 9; n++) {
        for (const idx of getSubBox(n)) {
            const cell = board[idx[0]][idx[1]]
            if (cell != ".") {
                // console.log(cell)
                if (!validityMod.has(cell)) {
                    validityMod.add(cell)
                } else {
                    return false
                 }
            }
        }
        validityMod = new Set();
        // console.log("-----")
    }
    return true
};