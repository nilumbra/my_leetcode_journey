int min(int arr[], int size){
    int m = INT_MAX;
    for (int i = 0; i < size; ++i) {
        if(arr[i] < m) {
            m = arr[i];
        }
    }
    return m;
}

int minimumTotal(int* triangle[], int triangleSize, int* triangleColSize){
   //int arr[] = {1,2,3,4,5};
   //printf("%d\n", max(arr ,5));
    //int end = triangleSize - 1;
    //printf("%d\n", max(triangle[end], triangleSize));
   
   //printf("%d\n", INT_MIN);
   if(triangleSize == 1) return triangle[0][0];
   triangle[1][0] += triangle[0][0];
   triangle[1][1] += triangle[0][0];
   if(triangleSize == 2) {
     return min(triangle[1], 2);
   }
   for (int i = 2;i < triangleSize;++i) {
     // printf("%d\n", triangleColSize[i]);
     // for first and last element on current row, do simple addition         
     triangle[i][0] += triangle[i-1][0];
     triangle[i][triangleColSize[i] - 1] += triangle[i-1][triangleColSize[i] - 2];
     printf("%d, %d ", triangle[i][0], triangle[i][triangleColSize[i] - 1]);
        // triangle
     for (int j = 1; j < triangleColSize[i]-1;++j) {
        int s = triangle[i][j];
        int t[] = {s+triangle[i-1][j-1], s+triangle[i-1][j]};
        //printf("j=%d (%d, %d), (%d, %d)\n", j, i-1, j-1, i - 1, j); 
        printf("(%d, %d)\n", s+triangle[i-1][j-1], s+triangle[i-1][j]); 
        triangle[i][j] = min(t, 2);
        
     } 
     printf("\n");
   }
    
    // get the maximum on the last row    
    int end = triangleSize - 1;
    return min(triangle[end], triangleSize);
    
    //return 0;
}