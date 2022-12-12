int removeDuplicates(int* nums, int numsSize){
    int dup = -101; // nums[i] \exists [-100, 100], use -101
    // use two pointer
    // i: the dummy pointer
    // j: the pointer indicating the position next non-duplica should be inserted
    // 
    // insert strategy: only insert if num[i] is not equal to cur
    int j = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == dup) continue;
        nums[j++] = nums[i];
        dup = nums[i]; // refresh the duplica test val
    }
    
    
    return j;
}