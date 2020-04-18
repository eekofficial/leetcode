# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        bijection = dict()
        str = str.split()
        if len(pattern) != len(str):
            return False
        for i in range(len(pattern)):
            if bijection.get(pattern[i]) == None:
                if str[i] in bijection.values():
                    return False
                bijection[pattern[i]] = str[i]
            else:
                if bijection[pattern[i]] != str[i]:
                    return False
        return True
