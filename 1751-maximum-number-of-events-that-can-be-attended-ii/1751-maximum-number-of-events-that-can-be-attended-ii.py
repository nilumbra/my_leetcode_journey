from bisect import bisect_right
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
       # this problem is identical to the job scheduling problem
       ### Subproblem
       # Given the events as an 3-tuple array sorted by start date
       # We can define the subproblem as follows:
       #   Assuming we have compute the max possible value for events[i+1:] with remaining attendable event k, what can we say about events[i:]
      n = len(events)
      events.sort(key=lambda x: x[0]) # sort by startDay
      dp = [[0] * (n + 1) for _ in range(k+1)]
      
      
      # i from k to 0
      #    j from n-1 to 0
      for i in reversed(range(k)):
        for j in reversed(range(n)):
          end = events[j][1]
          attend_i = bisect_right(events, end, key=lambda x:x[0])
          #print(f'attend_i = {attend_i}, @({i}, {j})')
          if attend_i <= n - 1:
            attend_i = attend_i if events[attend_i][0] > end else attend_i + 1
          #print(attend_i)
          #assert attend_i <= n, f'attned_i = {attend_i}, @({i}, {j})'
          dp[i][j] = max(
                          dp[i][j+1], # skip
                          dp[i+1][attend_i] + events[j][2]
                        )
          
      #print(dp)
      return dp[0][0]