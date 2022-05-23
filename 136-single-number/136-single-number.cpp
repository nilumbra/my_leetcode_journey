class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int mul, i; 
        
        mul = 0;
        for (int num : nums) {
            mul ^= num;
        }
        
        return mul;
    }
};