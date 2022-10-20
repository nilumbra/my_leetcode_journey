bool canJump(int* nums, int numsSize){
    int maxReachable = 0;
    // try traverse the entire arr, but stop short if current index is not reachable anymore
    for (int i = 0; i < numsSize - 1 && maxReachable >= i; ++i) {
        //printf("%d\n", nums[i]);
        maxReachable = (maxReachable < i + nums[i]) ? i + nums[i]: maxReachable; 
        //printf("%d\n", maxReachable);
    }
    
    return maxReachable >= numsSize - 1;
}