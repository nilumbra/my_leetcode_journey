class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first, curr_combination):
            if len(curr_combination) == k:
                res.append(curr_combination[:])
            
            for i in range(first, n + 1):
                curr_combination.append(i)
                
                backtrack(i + 1, curr_combination)
                
                curr_combination.pop()
                
        res = []
        
        backtrack(1, [])
        return res
        