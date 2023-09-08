function isGood(nums: number[]): boolean {
    // every number appears exactly once except the largest
    const mx = nums.length - 1 // this should be the largest num
    let xor = 0
    let mxN = 0
    for (let i = 0; i < nums.length - 1; xor ^= i++);
    
    for (const num of nums) {
        if (num > mx) {
            return false 
        } else if (num == mx) {
            mxN++
        } else {
            xor ^= num
        }
    }
    return xor == 0 && mxN == 2
};