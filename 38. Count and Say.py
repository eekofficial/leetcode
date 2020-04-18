#https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = '1'
        
        for i in range(2, n + 1):
            elem = s[0]
            count_elem = 1
            new_s = ''
            for i in range(1, len(s)):
                c = s[i]
                if c == elem:
                    count_elem += 1
                else:
                    new_s += str(count_elem) + elem
                    elem = c
                    count_elem = 1
            new_s += str(count_elem) + elem
            s = new_s
            
        return s
        
