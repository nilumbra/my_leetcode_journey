#77 Combinations
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def combi(n, k):
            if(k == 1 or k == 0):
                return [set([i]) for i in range(1, n+1)]
            
            combinations = []
            for combination in combi(n, k-1):
                # print(combination)
                for num in range(1, n+1):
                    if(num not in combination):
                        # print(str(num) + " not in " + str(combination))
                        # print(combination.copy()) 
                        comb = combination.copy()
                        comb.add(num)
                        if comb not in combinations:
                        # combination.extend([num])
                            combinations.append(comb) # .extend will mutate the original array!!!!!
            return combinations

        return [list(combination) for combination in combi(n, k) ]
        
if __name__ == '__main__':
    s = Solution()
    print(s.combine(18,4))