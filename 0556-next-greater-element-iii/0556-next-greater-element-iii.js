// convert the number to an array of integers

function numToArr(n) {
    var res = [];
    while (n > 0) {
        res.push(n % 10)
        n = Math.floor(n / 10)
    }
    
    res.reverse()
    return res;
}

function arrToNum(arr) {
    var num = 0
    var exp = 0
    for (let i = arr.length - 1; i >= 0; i--) {
        num += arr[i] * (10 ** exp)
        exp++
    }
    // console.log(num)
    return num 
}

// @Destrucive
function reverse(A, start, end) {
    var t = 0;
    
    while (start < end) {
        t = A[start]
        A[start] = A[end]
        A[end] = t
        
        start++
        end--
    }
}

/**
 * @param {number} n
 * @return {number}
 */
var nextGreaterElement = function(n) {
    var arr = numToArr(n)
    if (arr.length == 1)
        return -1
    
    var decreasing = true
    // can assume arr.length is at least 2
    for (let _ = arr.length - 1; _ > 0; _--) {
        if (arr[_ - 1] < arr[_]) {
            var i = _,
                _i = _ - 1
            decreasing = false
            
            break
        }   
    }
    
    if (decreasing) return -1
    
    // console.log(i, _i)
    
    // scan from right to i, find the first element a[j] such that a[j] > a[i - 1]
    // swap a[i-1] and a[j]
    for (let _ = arr.length -1; _ >= i; _--) {
        if (arr[_] > arr[_i]) {
            var t = arr[_]
            arr[_] = arr[_i]
            arr[_i] = t
            break
        }
    }
    
    // console.log(arr)
    // console.log(`reverse(arr, ${i}, ${arr.length - 1})`)
    reverse(arr, i, arr.length - 1)
    // scan for right to left, find the first a[i - 1] < a[i]. (implying a[i] to a[right] is decreasing)
    
    // console.log(arr)
    
    // reverse a[i:]
    var res = arrToNum(arr)

    return (res <= 2**31 - 1) ? res : -1
};