#https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        numbers_count = 0
        for n in range(L, R + 1):
            dec_number = n
            bin_number = ''
            while dec_number != 0:
                bin_number = str(dec_number % 2) + bin_number
                dec_number = dec_number // 2
            count_bits = 0
            for bit in bin_number:
                if bit == '1':
                    count_bits += 1
            if count_bits == 1:
                is_prime = False
            else:
                is_prime = True
            for i in range(2, int(count_bits ** (1/2)) + 1):
                if count_bits % i == 0:
                    is_prime = False
            if is_prime:
                numbers_count += 1
        return numbers_count
