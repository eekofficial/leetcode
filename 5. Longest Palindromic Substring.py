#https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        max_palindrome = 1
        max_low_start = 0
        max_high_start = 0
        for i in range(len(s) - 1):
            palindrome1 = self.palindrome_expand(s, i, i)
            palindrome2 = self.palindrome_expand(s, i, i + 1)
            if palindrome1 > max_palindrome:
                max_palindrome = palindrome1
                max_low_start = i
                max_high_start = i
            if palindrome2 > max_palindrome:
                max_palindrome = palindrome2
                max_low_start = i
                max_high_start = i + 1
        if max_low_start == max_high_start:
            lcs = s[max_low_start]
            max_palindrome -= 1
            low = max_low_start
            high = max_low_start
            while max_palindrome != 0:
                lcs = s[low - 1] + lcs + s[high + 1]
                low -= 1
                high += 1
                max_palindrome -= 2
        else:
            lcs = s[max_low_start] + s[max_high_start]
            max_palindrome -= 2
            low = max_low_start
            high = max_high_start
            while max_palindrome != 0:
                lcs = s[low - 1] + lcs + s[high + 1]
                low -= 1
                high += 1
                max_palindrome -= 2
        return lcs
    def palindrome_expand(self, s, low, high):
        if high > len(s) - 1 or low < 0:
            return 0
        elif low == high:
            return 1 + self.palindrome_expand(s, low - 1, high + 1)
        elif s[high] == s[low]:
            return 2 + self.palindrome_expand(s, low - 1, high + 1)
        else:
            return 0
