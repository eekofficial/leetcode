# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        min_len_s = float('inf')
        prefix = ''
        for s in strs:
            if len(s) < min_len_s:
                min_len_s = len(s)
        i = 0
        if min_len_s == float('inf'):
            return ''
    
        while i < min_len_s:
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return prefix
            prefix += strs[0][i]
            i += 1
        return prefix
                    
                    
                    
                    
                

