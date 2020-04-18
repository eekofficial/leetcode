#https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_dict = dict()
        for c in s:
            if letter_dict.get(c):
                letter_dict[c] += 1
            else:
                letter_dict[c] = 1
        count_pairs = 0
        exists_one = False
        for v in letter_dict.values():
            if v == 1:
                exists_one = True
            elif v % 2 == 0:
                count_pairs += v
            else:
                count_pairs += v - 1
                exists_one = True
        if exists_one:
            count_pairs += 1
        return count_pairs
