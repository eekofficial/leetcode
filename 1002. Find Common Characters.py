#https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        words_len = len(A)
        letter_dict = dict()
        letters = []
        for i in range(words_len):
            for j in range(len(A[i])):
                if letter_dict.get(A[i][j]):
                    letter_dict[A[i][j]][i] += 1
                else:
                    letter_dict[A[i][j]] = [0] * words_len
                    letter_dict[A[i][j]][i] += 1
        for letter, times in letter_dict.items():
            for i in range(min(times)):
                letters.append(letter)
        return letters
        
        
