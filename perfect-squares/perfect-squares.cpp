class Solution {
public:
    int numSquares(int n) {
      int arr[n+1];
      arr[0] = 0;
      for (int i = 1; i <= n; i++) {
        int minSteps = 100000;
        // for each i, find all the steps available
        for (int sqrt = 1; sqrt * sqrt <= i; sqrt++) {
          //.minimum steps need to get to (i - sqrt * sqrt)
          if (arr[i - sqrt * sqrt] + 1 < minSteps) 
            minSteps = arr[i - sqrt * sqrt] + 1;
        }
        arr[i] = minSteps;
      } 
      
      return arr[n];
    }
};