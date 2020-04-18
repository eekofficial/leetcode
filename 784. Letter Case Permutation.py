#https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        a = ord('a')
        z = ord('z')
        count_letters = 0
        S = S.lower()
        for c in S:
            if ord(c) >= a and ord(c) <= z:
                count_letters += 1
        if count_letters == 0:
            return [S]
        old_strings = {S[0]:1, S[0].upper():1}
        
        
        for i in range(1, len(S)):
            if ord(S[i]) >= a and ord(S[i]) <= z:
                new_strings = dict()
                for k in old_strings.keys():
                    new_strings["{}{}".format(k,S[i].upper())] = 1
                    new_strings["{}{}".format(k,S[i])] = 1
                old_strings = new_strings  
            else:
                new_strings = dict()
                for k in old_strings.keys():
                    new_strings["{}{}".format(k,S[i])] = 1
                old_strings = new_strings  
        return list(old_strings.keys())
            
        
            
        
                    
