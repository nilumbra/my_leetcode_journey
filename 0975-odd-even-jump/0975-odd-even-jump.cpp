class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        # brute-force: 
        # for i = 1 to N
        #   try series of jumps
        #   for j = 1 to 
        def nextSmallestGreater(arr:List[int], is_reverse=False) -> List[int] :
            """
            Produce an array of indices indicating the next smallest greater relative to each arr[i]
            """
            # sort by index
            arr_i_map = [(i, a) for i, a in enumerate(arr)]
            indices_sort = [i for i, a in sorted(arr_i_map, key=lambda x: x[1], reverse=is_reverse)] 
            # print(indices_sort) # 0 2 1 3 4
            # print(indices_sort)
            
            mStack = []
            res = [0] * len(arr)
            
            comp = lambda a, b: a < b if not is_reverse else a > b
            
            for idx in indices_sort:
              while mStack and mStack[-1] < idx:
                i_rev = mStack.pop()
                res[i_rev] = idx # i_res's next smallest greater is idx 
              mStack.append(idx)
            
            
            while mStack:
              res[mStack.pop()] = -1
            
            return res
            # print(res)
        odd =  nextSmallestGreater(arr)   
        even = nextSmallestGreater(arr,is_reverse=True)
        
        
        dpOdd = [False] * len(arr)
        dpEven = [False] * len(arr)
        dpOdd[-1] = True
        dpEven[-1] = True
        
        for i in range(len(arr)-2, 0, -1):
          dpOdd[i] = dpEven[odd[i]] if odd[i] > i else False
          dpEven[i] = dpOdd[even[i]] if even[i] > i else False
        
        dpOdd[0] = dpEven[odd[0]] if odd[0] > 0 else False
        # print(odd, even)
        # print(dpOdd, dpEven)
        
        return 1 if len(arr) == 1 else sum(dpOdd)