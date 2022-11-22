/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generateMatrix(int n, int* returnSize, int** returnColumnSizes){
  *returnSize = n;
  *returnColumnSizes = malloc(sizeof(int) * n);
  int **res = malloc(sizeof(int*) * n); // allocating memory for an array of int pointers
  
  // allocating memory for every row of returned 2d array
  for (int i = 0; i < n; i++) {
    (*returnColumnSizes)[i] = n;
    res[i] = malloc(sizeof(int) * n);
  } 
    
  
  
  int left = 0, right = n - 1;
  int top = 0, bot = n - 1;
  
  int x = 1;
  
  while(x <= n*n) {
    for (int j = left; j <= right ;j++, x++) 
      // printf("%d %d\n", top, j);
      res[top][j] = x;
    top++;
    
    for (int i = top; i <= bot ;i++, x++) 
      // printf("%d %d\n", i, right);
      res[i][right] = x;
    right--;
    
    for (int j = right; j >= left ;j--, x++)
      // printf("%d %d\n", bot, j);
      res[bot][j] = x;
    bot--;
    
    for (int i = bot; i >= top ;i--, x++) 
      // printf("%d %d\n", i, left);
      res[i][left] = x;
    left++;
  }
  
  
  return res;
}