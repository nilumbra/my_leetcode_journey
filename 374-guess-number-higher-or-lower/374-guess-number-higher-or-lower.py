# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n + 1
        while left < right:
            mid = int((left + right) / 2)
            p = guess(mid)
            if p == 0:
                return mid
            elif p == -1:
                right = mid
            else:
                left = mid + 1
                