

int singleNumber(int* nums, int numsSize){
        int mul, i; 
        
        mul = 0;
        for (i = 0; i < numsSize; i++) {
            mul ^= nums[i];
        }
        
        return mul;
}