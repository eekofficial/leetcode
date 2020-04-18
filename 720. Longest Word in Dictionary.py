# https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words_dict = {"":True}
        for word in words:
            words_dict[word] = True
        longest_word = ''
        for word in words:
            substr = ''
            contains = True
            for i in range(len(word) - 1):
                substr += word[i]
                if not words_dict.get(substr):
                    contains = False
                    break
            if contains:
                if len(word) > len(longest_word):
                    longest_word = word
                elif len(word) == len(longest_word) and word < longest_word:
                    longest_word = word
        return longest_word
