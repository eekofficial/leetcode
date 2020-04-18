#https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalpha():
                if s[right].isalpha():
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        return ''.join(s)
