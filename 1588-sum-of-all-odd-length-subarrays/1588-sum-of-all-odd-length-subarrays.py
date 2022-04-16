class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        Sum=0
        for i in range(1,len(arr)+1,2):
            j=0
            while j<=len(arr)-i:
                Sum+=sum(arr[j:j+i])
                j+=1
        return Sum