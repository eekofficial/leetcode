#https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        root = x ** (1 / 2)
        return int(root)
        
