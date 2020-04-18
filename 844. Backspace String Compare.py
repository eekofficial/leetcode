#https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        t = []
        for c in S:
            if c == '#':
                if len(s) >= 1:
                    s.pop()
            else:
                s.append(c)
        for c in T:
            if c == '#':
                if len(t) >= 1:
                    t.pop()
            else:
                t.append(c)
        if s == t:
            return True
        return False
