int removeElement(int* nums, int numsSize, int val){
    // use two pointers:
    // i: the dummy pointer for iteration
    // j: the pointer indicating the position next non-value element to be inserted at
    int j = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == val) continue;
        nums[j++] = nums[i];
    }
        
    return j;    
}