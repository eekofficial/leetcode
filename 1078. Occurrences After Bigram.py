#https://leetcode.com/problems/occurrences-after-bigram/

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        occurences = []
        text = text.split()
        for i in range(len(text) - 2):
            if text[i] == first and text[i + 1] == second:
                occurences.append(text[i + 2])
        return occurences
