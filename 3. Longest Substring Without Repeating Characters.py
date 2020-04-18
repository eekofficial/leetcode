# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        st = set()
        
        i = 0
        j = 0
        
        while j < len(s):
            if s[j] not in st:
                st.add(s[j])
                j += 1
                max_length = max(max_length, j - i)
            else:
                st.remove(s[i])
                i += 1
        return max_length
                
        
