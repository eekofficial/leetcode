# https://leetcode.com/problems/nim-game/

class Solution:
    def canWinNim(self, n: int) -> bool:
        return not n % 4 == 0
