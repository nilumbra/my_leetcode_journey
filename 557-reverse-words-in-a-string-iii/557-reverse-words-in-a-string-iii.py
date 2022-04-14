class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseString(s: List[str], start, end) -> None:
            """
            Do not return anything, modify s in-place instead.
            """
            
            while start < end:
                temp = s[start]
                s[start], s[end] = s[end], s[start]
                start, end = start + 1, end - 1
                
        start = end = 0
        s = list(s)
        n = len(s)
        
        for i in range(n):
            if i == n - 1:
                reverseString(s, start, end)
                
            if s[i] == ' ':
                reverseString(s, start, end - 1)
                start = end = i + 1
            else:
                end += 1
                
        return "".join(s)
                
                