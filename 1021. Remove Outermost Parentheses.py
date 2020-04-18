#https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ''
        count = 0
        for s in S:
            if s == '(':
                count += 1
            if count > 1:
                result += s
            if s == ')':
                count -= 1
        return result
            

                        
