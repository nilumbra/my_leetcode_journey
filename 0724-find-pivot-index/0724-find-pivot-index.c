

int pivotIndex(int* nums, int numsSize){
   int sum = 0;
   for (int i = 0; i < numsSize; i++) {
       sum += nums[i];
   }
   
   for (int i = 0, pre = 0;i < numsSize;++i) {
       if (pre == sum - nums[i] - pre) return i;
       pre += nums[i];
   }
   
   return -1;
}