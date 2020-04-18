#https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        bin_number = ''
        while num != 0:
            bin_number = str(num % 2) + bin_number
            num = num // 2
        bin_number = list(bin_number)
        for i in range(len(bin_number)):
            if bin_number[i] == '1':
                bin_number[i] = 0
            else:
                bin_number[i] = 1
        result = 0
        
        for n in bin_number:
            result = 2 * result + n
        
        return result
        
