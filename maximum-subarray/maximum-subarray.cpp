class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int mT = nums[0];
        int maxSum = mT;
        for (int i = 1; i < nums.size(); ++i) {
            mT = max(mT + nums[i], nums[i]);
            maxSum = max(mT, maxSum);
        }
        return maxSum;
    }
};