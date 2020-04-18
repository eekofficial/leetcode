#https://leetcode.com/problems/count-binary-substrings/

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        num_of_substr = 0
        for i in range(len(s) - 1):
            if s[i] == '0' and s[i + 1] == '1':
                num_of_substr += 1
                l = i - 1
                r = i + 1 + 1
                while l >= 0 and r < len(s):
                    if s[l] == '0' and s[r] == '1':
                        num_of_substr += 1
                    else:
                        break
                    l -= 1
                    r += 1
            elif s[i] == '1' and s[i + 1] == '0':
                num_of_substr += 1
                l = i - 1
                r = i + 1 + 1
                while l >= 0 and r < len(s):
                    if s[l] == '1' and s[r] == '0':
                        num_of_substr += 1
                    else:
                        break
                    l -= 1
                    r += 1
        return num_of_substr
