#https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            arr = []
        else:
            arr = [0]
            n -= 1
        
        for i in range(n, 0, -2):
            arr.append(-i)
            arr.append(i)
        return arr
