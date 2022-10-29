class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        S = list(map(lambda x: -x, stones))
        heapify(S)
        #print(S)
        
        while len(S) >= 2: 
          y = heappop(S)
          x = heappop(S)
          
          if x != y:
            heappush(S, y-x)
        
        return -S[0] if len(S) == 1 else 0