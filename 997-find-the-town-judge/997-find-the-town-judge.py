class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n == 1: return 1
        trusting = set()
        trusted = {}
        
        for truster,trustee in trust:
            trusting.add(truster)
            if trustee in trusted:
                trusted[trustee].add(truster)
            else:
                trusted[trustee] = set()
                trusted[trustee].add(truster)
        
        for trustee, trusters in trusted.items():
            if len(trusters) == n - 1 and trustee not in trusting:
                return trustee
        
        return -1
                