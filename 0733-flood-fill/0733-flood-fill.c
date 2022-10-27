


void fill(int** image, int row, int col, int sr, int sc, int tcolor, int color) {
  if (sr < 0 || sr >= row || sc < 0 || sc >= col || image[sr][sc] == color || image[sr][sc] != tcolor) return;
  image[sr][sc] = color; // fill
  fill(image, row, col, sr - 1, sc, tcolor, color); // top
  fill(image, row, col, sr + 1, sc, tcolor, color); // bottom
  fill(image, row, col, sr, sc - 1, tcolor, color); // left
  fill(image, row, col, sr, sc + 1, tcolor, color); // right
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int color, int* returnSize, int** returnColumnSizes){
  fill(image, imageSize, *imageColSize, sr, sc, image[sr][sc], color);
  *returnSize = imageSize;
  *returnColumnSizes = (int *)malloc(imageSize*sizeof(int));
  for(int i=0; i<imageSize;i++) (*returnColumnSizes)[i] = *imageColSize;
  
  return image;
}