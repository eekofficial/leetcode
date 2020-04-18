# https://leetcode.com/problems/hamming-distance/

class Solution:
    def convert_to_bin(self, x):
        bin_string = ''
        while x != 0:
            bin_string = str(x % 2) + bin_string
            x = x // 2
        return bin_string
    
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0
        x_bin = self.convert_to_bin(x)
        y_bin = self.convert_to_bin(y)
        
        if len(x_bin) < len(y_bin):
            x_bin = '0' * (len(y_bin)-len(x_bin)) + x_bin
        if len(y_bin) < len(x_bin):
            y_bin = '0' * (len(x_bin)-len(y_bin)) + y_bin
            
        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                hamming_distance += 1
        
        return hamming_distance
                
