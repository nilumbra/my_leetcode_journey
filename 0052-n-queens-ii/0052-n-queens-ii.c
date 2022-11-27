void dfs(int* res, int row, int n, int rowMask, int colMask, int fDiagMask, int bDiagMask) {
    
    // for a specific row, go through each cell (row, col) to see if a queen can be placed there
    for (int col = 0; col < n; col++) {
        
        // use bitmask to check if a queen has already been place at the same row / col / diagonals
        if (((1 << row)&rowMask) == 0 && ((1 << col)&colMask) == 0 && ((1 << (row+col))&fDiagMask) == 0 && ((1 << (row-col+n-1))&bDiagMask) == 0) {
            // if this is the bottom row, we found a feasible solution
            if (row == n - 1) (*res)++;
            // if not the bottom row, place a queen at cell (row, col) and update bitmask, then go to the next row
            else dfs(res, row+1, n, (1 << row)|rowMask, (1 << col)|colMask, (1 << (row+col))|fDiagMask, (1 << (row-col+n-1))|bDiagMask);
        }
    }
    return;
}

int totalNQueens(int n){
    int res = 0;
    dfs(&res, 0, n, 0, 0, 0, 0);
    return res;
}