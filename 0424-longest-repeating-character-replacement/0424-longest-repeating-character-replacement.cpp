class Solution {
public:
    int longestConsecutiveSubstringWithAtMostK_X(string s, int k, char c) {
      int left = 0, cnt = 0, m = 0;
      for (int i = 0; i < s.length(); i++) {
        if (s[i] != c) cnt++;
        while (cnt > k) {
          if (s[left] != c) 
             cnt--;
          left++;
        }
        
        m = max(m, i - left + 1);
      }
      
      return m;
    }
  
    int characterReplacement(string s, int k) {
      int longest = 0;
      for (int i = 0; i < 26; i++) {
        longest = max(longest, longestConsecutiveSubstringWithAtMostK_X(s, k, 'A'+i));
      }
      
      return longest;
    }          
};