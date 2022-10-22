

int search(int* nums, int numsSize, int target){
    int i = 0, j = numsSize - 1;
    int mid;
    while(i <= j) {
        mid = (i + j) / 2;
        if (nums[mid] == target) {
            return mid;
        } 
        if (nums[mid] > target) {
            j = mid - 1;
        } else {
            i = mid + 1;
        }
    }
    
    return -1;
}