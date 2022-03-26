class Solution {
    public int search(int[] nums, int target) {
        int pivot, l = 0; int r = nums.length - 1;
        //nums[mid] != target &&
        while (l <= r){
            pivot = (l + r)/2;
            if (nums[pivot] == target) return pivot;
            if (target < nums[pivot]){
                r = pivot - 1;
            }else{
                l = pivot + 1;   
            }
        }
        return -1;
    }
}