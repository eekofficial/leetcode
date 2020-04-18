#https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        num = N
        bin_number = ''
        if num == 0:
            bin_number = '0'
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
        
