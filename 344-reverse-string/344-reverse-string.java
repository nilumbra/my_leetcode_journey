class Solution {
    public void reverseString(char[] s) {
        int start = 0, end = s.length - 1;
        while(start < end){
            swap(s, start, end);
            start++;
            end--;
        }
    }
    private void swap(char[] s, int start, int end){
        char t = s[start];
        s[start] = s[end];
        s[end] = t;
    }
    
}