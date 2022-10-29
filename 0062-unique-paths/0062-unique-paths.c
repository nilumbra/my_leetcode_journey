

int uniquePaths(int m, int n){
  int u[n];
  for (int j=0;j<n;j++)
    u[j] = 1;

  for (int i=1;i<m;i++) {
    for (int j=1;j<n;j++){
      u[j] = u[j] + u[j-1];
    }
  }
  
  return u[n-1];
}