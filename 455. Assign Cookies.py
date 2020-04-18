# https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        res = 0
        left = 0
        right = 0
        while right < len(s) and left < len(g):
            if s[right] >= g[left]:
                res += 1
                left += 1
                right += 1
            else:
                right += 1
        return res
