class Solution {
public:
    int dp(int n, map<int, int>m) { 
        if (n == 0) return 0;
        if (n == 1) return 1;

        if (m.count(n) > 0) return m[n];
        else return dp(n - 1, m) + dp(n - 2, m);
    };

    int fib(int n) {
        map<int, int> m; 
  
        return dp(n, m);
    }   
    
};