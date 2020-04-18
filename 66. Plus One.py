# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''
        for digit in digits:
            number += str(digit)
        numbers = str(int(number) + 1)
        number_list = list()
        for num in numbers:
            number_list.append(num)
        return number_list
            
        
    
        
