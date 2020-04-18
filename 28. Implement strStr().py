# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle:
                return i
            if haystack[i] == needle[0]:
                equal = True
                left = i + 1
                right = i + len(needle) - 1
                left_n = 1
                right_n = len(needle) - 1
                if right >= len(haystack) or left >= len(haystack):
                    equal = False
                    break
                while left_n <= right_n:
                    if haystack[left] != needle[left_n]:
                        equal = False
                        break
                    if haystack[right] != needle[right_n]:
                        equal = False
                        break
                    left += 1
                    left_n += 1
                    right -= 1
                    right_n -= 1
                if equal:
                    return i
            i += 1
        return -1
            
        
