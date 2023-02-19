class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        // preprocessing nums2 using a stack and map
        // store in the map {num, next_greater_num}
        unordered_map<int, int> nxt_gt_map;
        stack <int> prev;
       
        for (int i: nums2) {
          while(!prev.empty() && prev.top() < i) {
            int num_small_found = prev.top();
            prev.pop();
            nxt_gt_map[num_small_found] = i; // next greater ele of num_small_found is i
          }
          
          prev.push(i);
        }
        
        while(!prev.empty()) {
          int no_next_greater = prev.top();
          nxt_gt_map[no_next_greater] = -1;
          prev.pop();
        }
        
        vector<int> res;
        for (int j: nums1) {
          res.push_back(nxt_gt_map[j]);
        }
      
        return res;
    }
};