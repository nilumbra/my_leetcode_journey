int max(int a, int b) {
  return a > b ? a : b;
}

int longestCommonSubsequence(char * text1, char * text2){
  int i = 0, j = 0;
  int M = strlen(text1), N = strlen(text2);
  int L[M+1][N+1];
  for (i = 0; i < M+1; i++) {
    L[i][0] = 0;
  }
  
  for (j = 0; j < N+1; j++) {
    L[0][j] = 0;
  }
  
  for(i = 1; i < M+1; i++) {
    for(j = 1; j < N+1; j++) {
      if (text1[i-1] == text2[j-1]) 
        L[i][j] = L[i-1][j-1] + 1;
      else 
        L[i][j] = max(L[i][j-1], L[i-1][j]);   
      // printf("(%d, %d), %d\n", i, j, L[i][j]);
    }
  }
  
  return L[M][N];
}