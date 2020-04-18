#https://leetcode.com/problems/binary-gap/

class Solution:
    def binaryGap(self, N: int) -> int:
        bin_number = ''
        while N != 0:
            bin_number = str(N % 2) + bin_number
            N = N // 2
        longest = 0
        current_i = 0
        s = bin_number.find('1')
        if s == -1:
            return 0
        for i in range(s + 1, len(bin_number)):
            if bin_number[i] == '1':
                distance = i - current_i
                longest = max(longest, distance)
                current_i = i
        return longest

