#https://leetcode.com/problems/rotated-digits/

class Solution:
    def rotatedDigits(self, N: int) -> int:
        good_numbers = 0
        for i in range(1, N + 1):
            n = str(i)
            if ('2' in n or '5' in n or '6' in n or '9' in n) and '3' not in n and '4' not in n and '7' not in n:
                good_numbers += 1
        return good_numbers
