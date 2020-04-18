#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        no_dup = True
        while no_dup:
            no_dup = False
            new_s = ''
            i = 0
            while i < len(S):
                if i < len(S) - 1 and S[i] == S[i+1]:
                    i += 2
                    no_dup = True
                else:
                    new_s += S[i]
                    i += 1
            S = new_s
            new_s = ''
        return S
            
