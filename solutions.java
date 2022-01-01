package solutions;
import java.util.Arrays;
public class solutions{
    //
    public static class NextPermutation{
        public void Next(int[] nums){
            int i = nums.length - 2;
            while(i >= 0 && nums[i] >= nums[i+1]){
                i--;
            }

            int j = nums.length - 1;
            if(i >= 0){
                while(j > i && nums[j] <= nums[i]){
                    j--;
                }
                swap(nums, i, j);
            }
            reverse(nums, i+1);
            System.out.println(Arrays.toString(nums));
        }

        public void swap(int[] nums, int i, int j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
   
        private void reverse(int[] nums, int start){
            int i = start;
            int j = nums.length - 1;
            while(i<j){
                swap(nums, i, j);
                i++;
                j--;
            }
        }
    }  

    //3. Longest Substring Without Repeating Characters
    public static class LengthOfLongestSubstring{
        public int lengthOfLongestSubstring(String s) {
        int n = s.length(), ans = 0;
        int[] index = new int[128];
        for(int j = 0, i = 0; j < n; j++){
            i = Math.max(index[s.charAt(j)], i);
            ans = Math.max(ans, j - i + 1);
            index[s.charAt(j)] = j + 1;
        }
        return ans;
        }  
    }

    //567. Permutation in String
    public static class PermutationInString{
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
    //733.Flood Fill (Using DFS)
    public static class FloodFill {
        public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
            int color = image[sr][sc];
            if(color != newColor) dfs(image, sr, sc, color, newColor);
            return image;
        }
        
        public void dfs(int[][] image, int r, int c, int color, int newColor){
            if(image[r][c] == color){
                image[r][c] = newColor;
                if(r >= 1) dfs(image, r - 1, c, color, newColor);
                if(c >= 1) dfs(image, r, c - 1, color, newColor);
                if(r+1 < image.length) dfs(image, r+1, c, color, newColor);
                if(c+1 < image[0].length) dfs(image, r, c+1, color, newColor);
            }
        }
    }
}
