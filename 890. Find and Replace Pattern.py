#https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern = self.count_letters(pattern)
        match = []
        
        for word in words:
            if self.count_letters(word) == pattern:
                match.append(word)
        return match
    
    def count_letters(self, word):
        s = ''
        elem = word[0]
        count = 1
        elems = set()
        elem_type = dict()
        elem_type_i = 0
        for i in range(1, len(word)):
            if word[i] == elem:
                count += 1
            else:
                if elem_type.get(elem) != None:
                    s += str(count) + '.' + str(elem_type[elem]) + '.'
                else:
                    elem_type[elem] = elem_type_i
                    s += str(count) + '.' + str(elem_type[elem]) + '.'
                    elem_type_i += 1
                elem = word[i]
                count = 1
        if elem_type.get(elem) != None:
            s += str(count) + '.' + str(elem_type[elem]) + '.'
        else:
            elem_type[elem] = elem_type_i
            s += str(count) + '.' + str(elem_type[elem]) + '.'
            elem_type_i += 1
        return s
