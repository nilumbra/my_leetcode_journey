type Fn = (...params: any) => any

function memoize(fn: Fn): Fn {
    const memo = new Map()
    return function(...args) {
        const key = args.length === 1 ? args[0] : '(' + args[0] + ',' + args[1] + ')' 
        // return cache
        if (memo.has(key)) {
            return memo.get(key)
        }
        
        const ret = fn(...args)
        memo.set(key, ret)
        return ret
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */