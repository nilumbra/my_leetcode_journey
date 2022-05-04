import bisect
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        """
        The returned insertion point i partitions the array a into two halves so that 
        all(val < x for val in a[lo : i]) for the left side and 
        all(val >= x for val in a[i : hi]) for the right side.
        """
        arr2.sort()
        count = 0
        l = len(arr2)
        for num in arr1:
            i = bisect.bisect_left(arr2, num)
            ok = True
            if i > 0:
                ok &= (num - arr2[i - 1] > d)
            if i < l:
                ok &= (arr2[i] - num > d)
                
            count += ok
        
        return count
            