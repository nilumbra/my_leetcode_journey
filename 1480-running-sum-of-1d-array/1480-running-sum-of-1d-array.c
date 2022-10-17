/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize){
    *returnSize = numsSize;
    //printf("%d", numsSize);
    //int * sum = malloc(numsSize * sizeof(int));
    //int pre = nums[0];
    //sum[0] = nums[0];
    for(int i = 1; i < numsSize;++i) {
        nums[i] += nums[i-1]; // copy the value
        //sum[i] += sum[i-1]; // accumulate
        //printf("%d\n", sum[i]);
    }
    //if(numsSize == 1) return nums;
    //for (int i = 0;)
    return nums;
}