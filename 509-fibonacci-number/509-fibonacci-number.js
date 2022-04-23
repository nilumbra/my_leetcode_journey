/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    if (n == 0) {
        return 0
    } 
    
    if (n == 1) {
        return 1
    }
    var [__f, _f] = [0, 1],
               f  = 0;
    
    for (let i = 2; i <= n; i++) {
        f = __f + _f;
        __f = _f;
        _f = f
    }
    
    return f
};