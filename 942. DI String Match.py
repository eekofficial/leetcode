#https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        d = len(S)
        i = 0
        result = []
        for c in S:
            if c == 'D':
                result.append(d)
                d -= 1
            if c == 'I':
                result.append(i)
                i += 1
        if S[-1] == 'D':
            result.append(d)
        else:
            result.append(i)
        return result
        
