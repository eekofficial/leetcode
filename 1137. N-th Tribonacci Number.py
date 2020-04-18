#https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        first = 0
        second = 1
        third = 1
        for i in range(3, n + 1):
            n = first + second + third
            first = second
            second = third
            third = n
        return n
