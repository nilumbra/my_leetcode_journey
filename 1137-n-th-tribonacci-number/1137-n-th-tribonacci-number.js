/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
    switch (n) {
        case 0: return 0
        case 1: return 1
        case 2: return 1
    }
    
    var ___t = 0, __t = 1, _t = 1, t = 0;
    
    for (let i = 3; i <= n; i++) {
        t = ___t + __t + _t;
        ___t = __t;
        __t = _t;
        _t = t;
    }
    
    return t
};