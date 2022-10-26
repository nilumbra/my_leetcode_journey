

int jump(int* nums, int numsSize){
    int jumps = 0, currentJumpEnd = 0, farthest = 0;
    
    int i = 0;
    while(i < numsSize - 1) {
      
      if(i + nums[i] > farthest) {
        farthest = i + nums[i];
      }
      
      if(i == currentJumpEnd) {
        jumps++;
        currentJumpEnd = farthest;
      } 
      i++;
    }
    
    return jumps;
}