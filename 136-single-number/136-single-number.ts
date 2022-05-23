function singleNumber(nums: number[]): number {
    var mul :number = 0;
    nums.forEach(function(num:number){
        mul ^= num;   
    })
    
    return mul;
};