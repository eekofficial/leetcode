#https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        a = list(A)
        b = list(B)
        if a == b:
            return True
        for i in range(len(a)):
            a.append(a.pop(0))
            if a == b:
                return True
        return False
            
        
