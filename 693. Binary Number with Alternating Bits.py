#https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_number = ''
        while n != 0:
            bin_number = str(n % 2) + bin_number
            n = n // 2
        for i in range(len(bin_number) - 1):
            if bin_number[i] == bin_number[i + 1]:
                return False
        return True
