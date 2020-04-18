#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum_of_strings = 0
        chars_dict = collections.defaultdict(int)
        for c in chars:
            chars_dict[c] += 1
        for word in words:
            good = True
            word_dict = collections.defaultdict(int)
            for c in word:
                word_dict[c] += 1
            for c, times in word_dict.items():
                if times > chars_dict[c]:
                    good = False
                    break
            if good:
                sum_of_strings += len(word)
        return sum_of_strings
            
