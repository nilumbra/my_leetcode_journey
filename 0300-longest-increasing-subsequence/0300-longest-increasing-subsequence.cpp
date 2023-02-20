void printSet(set<int> &sub) {
  for (auto i: sub) cout << i << ' ';
  cout << "\n";
}
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {   
      set<int> sub; // maintain a sorted list S, s.t. len(S) == # of longest increasing subsequence found
      
       // for each nums[i]
       // expand the S if nums[i] > max(S)
       // otherwise if nums[i] is not in S already, replace the next greater element of nums[i] with nums[i]
       // notice the reason we can do the replacement is because by replacing the greater element, we can create more 'space' for future elements in the array. This can be prove more rigorously with mathematical induction
      for (int a: nums) {
        auto it = sub.upper_bound(a);
        if (it != sub.end()) { 
          int val = *it;
          // it a already exists in the set, this should be a no-op
          if (sub.count(a) == 0) sub.erase(val); 
          // cout << "erase " << val << '|' ;
        }
        sub.insert(a);
        // printSet(sub);
      }
        
      return sub.size();
    }
};