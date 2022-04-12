
/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function(salary) {
    var mx = -Infinity,
        mn = Infinity;
    for (const num of salary) {
        mx = num > mx ? num : mx;
        mn = num < mn ? num : mn;
        
    }
    
    var sum = 0,
        count = 0;
    for (const num of salary) {
        if (num == mx || num == mn) {
            // console.log(num)
            count++;
            continue
        } else {
            sum += num;
        }
    }
    
    return +((sum / (salary.length - count)).toFixed(5)) 
    
};