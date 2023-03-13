class Solution {
    public double myPow(double x, int n) {
        boolean neg = n < 0 ? true : false;
        long _n = Math.abs((long) n);
        double ans = 1;
        
        // 繰り返し二乗法
        while (_n > 0) { // this loops runs for floor(lg(n)) + 1 times
            if ((_n & 1) == 1) {
              ans *= x;
            }
            x *= x;
            _n = _n >> 1;
        }
        
        return neg ? (1 / ans): ans;
    }
}