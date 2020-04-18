#https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        amount = 0
        r_amount = 0
        l_amount = 0
        for c in s:
            if c == 'R':
                r_amount += 1
            elif c == 'L':
                l_amount += 1
            
            if l_amount == r_amount:
                amount += 1
                l_amount = 0
                r_amount = 0
        return amount
