#https://leetcode.com/problems/excel-sheet-column-number/

 class Solution:
    def titleToNumber(self, s: str) -> int:
        s = list(s)
        i = 0
        result = 0
        while len(s) > 0:
            result += (ord(s.pop()) - ord('A') + 1) * (26 ** i)
            i += 1
        return result
