class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # d[i] = min (d[i - 1] + cost[i - 1], d[i - 2] + cost[i - 2])
        __, _ = 0, 0
        curr = 0
        i = 2
        while i <= len(cost):
            curr = min(__ + cost[i - 2], _ + cost[i - 1])
            __, _ = _, curr
            i += 1

        return curr
        