# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, n: int) -> str:
        column_title = ''
        while n != 0:
            n -= 1
            column_title = chr(ord('A') + n % 26) + column_title
            n //= 26
        return column_title
