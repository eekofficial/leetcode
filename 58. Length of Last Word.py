# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        max_len = 0
        last_word = ''
        word = ''
        for c in s:
            if c.isalnum():
                word += c
            else:
                if word != '':
                    last_word = word
                    word = ''
        if word != '':
            last_word = word
            word = ''
        return len(last_word)
