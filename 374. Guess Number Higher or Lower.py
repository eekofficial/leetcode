#https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while True:
            mid = (low + high) // 2
            hint = guess(mid)
            if hint == 0:
                return mid
            elif hint == 1:
                low = mid + 1
            else:
                high = mid - 1
