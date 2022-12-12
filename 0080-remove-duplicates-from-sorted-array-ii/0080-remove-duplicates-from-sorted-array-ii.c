int removeDuplicates(int* nums, int numsSize){
    // use two pointer
    // give duplicas a second chance
    int chance = 1;
    int dup = -10001;
    int j = 0; // insertion index
    
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != dup) {
            nums[j++] = nums[i];
            chance = 1;
            dup = nums[i];
        } else {
            if (chance) {
                nums[j++] = nums[i];
                chance--;
            } 
        }
        // skip... 
    }
    
    return j;
}