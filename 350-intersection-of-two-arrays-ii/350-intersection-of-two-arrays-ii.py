from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        number_book1 = defaultdict(int)
        number_book2 = defaultdict(int)
        
        for n in nums1:
            number_book1[n] += 1
        for m in nums2:
            number_book2[m] += 1
        
        nums1 = set(number_book1.keys())
        nums2 = set(number_book2.keys())
        
        comm = nums1 & nums2
        
        res = []
        for n in comm:
            rep = min(number_book1[n], number_book2[n])
            res.extend([n] * rep)
        
        return res
        
            