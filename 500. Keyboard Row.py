# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set('qwertyuiop')
        second_row = set('asdfghjkl')
        third_row = set('zxcvbnm')
        new_words = []
        for word in words:
            lower_word = word.lower()
            can = True
            if lower_word[0] in first_row:
                for i in range(1, len(word)):
                    if lower_word[i] not in first_row:
                        can = False
                        break
            elif lower_word[0] in second_row:
                for i in range(1, len(word)):
                    if lower_word[i] not in second_row:
                        can = False
                        break
            elif lower_word[0] in third_row:
                for i in range(1, len(word)):
                    if lower_word[i] not in third_row:
                        can = False
                        break
            else:
                can = False
            if can:
                new_words.append(word)
        return new_words
                
