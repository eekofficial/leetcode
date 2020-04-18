#https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_number = ''
        bits = 0
        while n != 0:
            bin_number = str(n % 2) + bin_number
            n = n // 2
        for bit in bin_number:
            if bit == '1':
                bits += 1
        return bits
