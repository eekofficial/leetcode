#https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = 0
        for s in S:
            if s in J:
                jewels += 1
        return jewels
