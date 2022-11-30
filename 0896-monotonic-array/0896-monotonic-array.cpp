class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        if (size(nums) <= 2) 
          return true;
        
        int flag = 0;
      
        for (int i = 0; i < size(nums) - 1; i++) {
          if (flag == 0) {
            if (nums[i] == nums[i + 1]) 
              continue;
            else if (nums[i] > nums[i + 1]) 
              flag = 1; // monotonically increasing
            else 
              flag = -1; // monotonically decreasing
            
            continue;
          }
          
          if ((flag * (nums[i] - nums[i+1])) < 0)
            return false;
          
        }
        return true;
    }
};