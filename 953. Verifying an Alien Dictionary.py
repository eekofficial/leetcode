#https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            j = 0
            sort = True
            equal = True
            while j < len(words[i]) and j < len(words[i + 1]):
                if order.find(words[i][j]) > order.find(words[i + 1][j]):
                    sort = False
                    equal = False
                    break
                elif order.find(words[i][j]) < order.find(words[i + 1][j]):
                    sort = True
                    equal = False
                    break
                j += 1
            if (equal and len(words[i]) > len(words[i + 1])) or not sort:
                return False
        return True
