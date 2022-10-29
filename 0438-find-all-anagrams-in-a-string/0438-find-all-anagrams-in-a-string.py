class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
      k = len(p)
      ans = []
      
      pAna = Counter(p)
      keys = pAna.keys()
      def checkEqual(pAna, sAna):
        nonlocal keys
        for k in keys:
          if pAna[k] != sAna[k]:
            return False
        return True
      
      sAna = Counter(s[:k])
      if checkEqual(pAna,sAna):
        ans.append(0)
        
      for i in range(1, len(s) - k + 1):
        sAna[s[i-1]] -= 1
        sAna[s[i+k-1]] += 1
        if checkEqual(pAna, sAna):
          ans.append(i)
          
      return ans
        