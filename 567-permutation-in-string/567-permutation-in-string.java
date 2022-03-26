class Solution {
    public boolean checkInclusion(String s1, String s2) {
    if(s1.length() > s2.length()) return false; // If s1 is longer than s2, no permutation of s1 is a substring of s2.
                
            int[] s1map = new int[26];
            int[] s2map = new int[26];
            
            for(int i = 0; i < s1.length();i++){
                s1map[s1.charAt(i) - 'a']++;
                s2map[s2.charAt(i) - 'a']++;
            }
            
            for(int i = 0; i < s2.length() - s1.length();i++){
                if(matches(s1map, s2map)) return true;
                s2map[s2.charAt(i + s1.length()) - 'a']++;
                s2map[s2.charAt(i) - 'a']--;
            }
            
            return matches(s1map, s2map);
        }
            
        public boolean matches(int[] m1, int[]m2){
            for(int i = 0;i < 26;i++){
                if(m1[i] != m2[i]){
                    return false;
                }
            }
            return true;
        }
}