class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int end = 0;
        int shortest = 201;
        for (string s: strs) {
          shortest = size(s) < shortest ? size(s) : shortest;
        }        
        
        for (int i = 0; i < shortest; i++) {
          char x = strs[0][i];
          for (int j = 0; j < size(strs); j++) {
            if (x != strs[j][i]) {
              return strs[0].substr(0, end);
            }
          }
          end++;
        }
          
        return strs[0].substr(0, end);
    }
};