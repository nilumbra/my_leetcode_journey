

int lengthOfLIS(int* nums, int numsSize){
  int L[numsSize+1];
  for(int i = 0; i < numsSize+1; L[i++]=0)
    ;
  
  int maxLen = 0;
  for(int i = 1; i < numsSize+1;++i) {
    for(int j = 0; j < i;++j) {
      if(j == 0 || nums[j-1] < nums[i-1]) {
        L[i] = L[j]+1 > L[i] ? L[j]+1: L[i];
      }
    }
    maxLen = L[i] > maxLen ? L[i] : maxLen;
  }
  
  // for (int i = 0; i < numsSize+1;++i){
  //   printf("%d ", L[i]);
  // }
  // printf("\n");
  return maxLen;
}