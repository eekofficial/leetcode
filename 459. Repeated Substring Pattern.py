#https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)):
            for j in (i + 1, len(s)):
                tmp = s[i:j] 
                if tmp != s and (len(s) // len(tmp)) * tmp == s:
                    return True
        return False
