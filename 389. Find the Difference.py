# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        bits_s = 0
        bits_t = 0
        for c in s:
            bits_s += ord(c)
        for c in t:
            bits_t += ord(c)
        return chr(abs(bits_s - bits_t))

