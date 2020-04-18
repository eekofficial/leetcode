#https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = res * 2 + n % 2
            n //= 2
        return res
