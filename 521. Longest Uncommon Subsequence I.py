#https://leetcode.com/problems/longest-uncommon-subsequence-i/

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return max(len(a), len(b))
        for i in range(len(a)):
            if a[i] != b[i]:
                return(len(a))
        return -1
