class Solution {
public:
    // store the nxt = nums[curr] to nums[nxt],
    // if nums[nxt] == nxt, return nxt 
    int store(vector<int>& nums, int curr) {
        if (nums[curr] == curr) return curr;
        int nxt = nums[curr];
        nums[curr] = curr;
        return store(nums, nxt);
    }
    
    int findDuplicate(vector<int>& nums) {
        return store(nums, 0);
    }
};