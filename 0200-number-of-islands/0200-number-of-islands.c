
void dfs(char** grid, int row, int col, int i, int j) {
  if (i < 0 || i >= row || j < 0 || j >= col || grid[i][j] == '0') return;
  grid[i][j] = '0';
  dfs(grid, row, col, i-1, j);
  dfs(grid, row, col, i+1, j);
  dfs(grid, row, col, i, j-1);
  dfs(grid, row, col, i, j+1);
}

int numIslands(char** grid, int gridSize, int* gridColSize){
  int islands = 0;
  //*gridColSize = sizeof(grid[0]) / sizeof(int);
  for (int i = 0; i < gridSize; i++) {
    for (int j = 0; j < *gridColSize ; j++) {
      if (grid[i][j] == '1') {
        islands++;
        dfs(grid, gridSize, *gridColSize, i, j);
      }
//      printf("%c ", grid[i][j]);
    }
//    printf("%\n");
  }
  return islands;
}