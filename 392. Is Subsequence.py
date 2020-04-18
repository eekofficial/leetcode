#https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub_i = 0
        s_i = 0
        if len(s) == 0:
            return True
        while sub_i < len(s) and s_i < len(t):
            if t[s_i] == s[sub_i]:
                if sub_i == len(s) - 1:
                    return True
                sub_i += 1
                s_i += 1
            else:
                s_i += 1
        return False
