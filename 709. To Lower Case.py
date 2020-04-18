#https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLowerCase(self, str: str) -> str:
        left_upper_border = ord('A')
        right_upper_border = ord('Z')
        delta = ord('a') - ord('A')
        new_str = ""
        for s in str:
            if ord(s) >= left_upper_border and ord(s) <= right_upper_border:
                new_str += chr(ord(s) + delta)
            else:
                new_str += s        
        return new_str
            
        
        
