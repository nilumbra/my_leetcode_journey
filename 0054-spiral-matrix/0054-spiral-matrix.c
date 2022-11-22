/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* spiralOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize){
  int * result = (int *) malloc(matrixSize*(*matrixColSize)*sizeof(int));
  
  int left = 0, right = *matrixColSize - 1;
  int up = 0, bottom = matrixSize - 1;  
  int idx = 0;
  
  while(left <= right && up <= bottom) {
    for (int j = left; j <= right; j++) 
      result[idx++] = matrix[up][j];
      // printf("%d %d\n", up, j);
    // up++;
    
    for (int i = up+1; i <= bottom; i++)  // move down
      result[idx++] = matrix[i][right];
      // printf("%d %d\n", i, right);
    // right--;
    
    for (int j = right-1; j > left && up != bottom; j--)  // move left
      result[idx++] = matrix[bottom][j];
      // printf("%d %d\n", bottom, j);
    // bottom--;
    
    for (int i = bottom; i > up && left != right; i--)  // move up
      result[idx++] = matrix[i][left];
      // printf("%d %d\n", i, left);
    up++; right--; bottom--; left++;
  }
  
  *returnSize = idx;
  return result;
}