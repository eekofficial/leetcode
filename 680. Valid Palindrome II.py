#https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        count_not_equal = 0
        s = list(s)
        indexes = self.find_not_equal(s)
        if indexes:
            indexes1 = self.find_not_equal(s, indexes[0])
            indexes2 = self.find_not_equal(s, indexes[1])
            if indexes1 and indexes2:
                return False
            else:
                return True
        else:
            return True
        
        return False
    
    def find_not_equal(self, s, delete=-1):
        m = []
        m += s
        if delete != -1:
            m.pop(delete)
        for i in range(len(m) // 2):
            if m[i] != m[len(m) - 1 - i]:
                return ((i, len(m) - 1 - i))
        return False
                
