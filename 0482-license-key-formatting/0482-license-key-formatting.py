class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        S = []
        K = k
        for c in reversed(s):
          if c == '-':
            continue
          else:
            k -= 1
            S.append(c.upper())
            if k == 0:
              S.append('-')
              k = K
        
        if S and S[-1] == '-':
          S.pop()
          
        return ''.join(reversed(S))