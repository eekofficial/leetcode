#https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        letter = ''
        result = ''
        for l in s:
            if l == '#':
                letters_before_i = ''
                letter_after_j = ''
                for i in range(len(letter) - 2):
                    letters_before_i += letter[i]
                for i in range(len(letter) - 2, len(letter)):
                    letter_after_j += letter[i]
                if letters_before_i:
                    for c in letters_before_i:
                        result += chr(ord('a') + int(c) - 1)
                result += chr(ord('a') + int(letter_after_j) - 1)
                letter = ''
            else:
                letter += l
        for c in letter:
            result += chr(ord('a') + int(c) - 1)
        return result
        
