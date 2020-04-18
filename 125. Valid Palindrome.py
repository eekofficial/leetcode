#https://leetcode.com/problems/valid-palindrome/:

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = re.sub('\W', '', s).lower()
        print(res)
        if res == res[::-1]:
            return True
        else:
            return False
    
