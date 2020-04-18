#https://leetcode.com/problems/shortest-completing-word/

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:
        licensePlate = licensePlate.lower()
        string = ''
        for c in licensePlate:
            if c.isalpha():
                string += c
        s_dict = dict()
        for c in string:
            if s_dict.get(c):
                s_dict[c] += 1
            else:
                s_dict[c] = 1
        min_len = float('inf')
        min_len_word = None
        for word in words:
            word_dict = dict()
            for c in word:
                if word_dict.get(c):
                    word_dict[c] += 1
                else:
                    word_dict[c] = 1
            can = True
            for c, times in s_dict.items():
                if not word_dict.get(c) or times > word_dict[c]:
                    can = False
            if can and len(word) < min_len:
                min_len = len(word)
                min_len_word = word
        return min_len_word
