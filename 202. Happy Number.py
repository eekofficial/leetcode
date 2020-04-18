#https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        if n > 0:
            visited = set()
            while n != 1:
                if n in visited:
                    return False
                visited.add(n)
                q_sum = 0
                while n > 0:
                    q_sum += (n % 10) ** 2
                    n = n // 10
                n = q_sum
            return True
        else:
            return False
        
