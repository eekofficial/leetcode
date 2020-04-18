class Solution:
    def countBits(self, num: int):
        count_bits = [0]
        bin_number = ['0']
        for i in range(0, num):
            res = self.count_ones(bin_number)
            bin_number = res[0]
            count_bits.append(res[1])
        return count_bits
            
        
        
    def count_ones(self, bin_num):
        count_ones = 0
        carry = 1
        for i in range(len(bin_num) - 1, -1, -1):
            if bin_num[i] == '1' and carry:
                bin_num[i] = '0'
                carry = 1
            elif carry:
                bin_num[i] = '1'
                count_ones += 1
                carry = 0
            elif bin_num[i] == '1':
                count_ones += 1
        if carry:
            bin_num = ['1'] + bin_num
            count_ones += 1
        return (bin_num, count_ones)
