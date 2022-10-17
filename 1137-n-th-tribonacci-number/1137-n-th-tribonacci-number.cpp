class Solution {
public:
    int memo[38] = {0};
    int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        if (memo[n] != 0) return memo[n];
        
        return memo[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3);
        
        // if (n > 2 && memo[n] == 0) { // n > 2 and it's the first computation of tri(n)
        //     cout << "@ " << n << endl;
        //     memo[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3);
        //     cout << memo[n] << endl;
        //     return memo[n];
        // } else {
        //     cout << "called" << endl;
        //     return memo[n];
        // }
        // for(int n : memo) cout << n;
        // cout << memo;
    }
};