#https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address = ''
        for s in address:
            if s == '.':
                new_address += '[.]'
            else:
                new_address += s
        return new_address
                
