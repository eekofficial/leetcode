#https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int):
            x = str(x)
            while (x != '0') & (x[-1] == '0'):
                x = x[:-1]  
            y = ''
            for i in range(len(x) - 1, -1, -1):
                if x[i] == '-':
                    y = int('-' + y)
                    if (y >= -2 ** 31) and (y <= 2 ** 31):
                        return y
                    else:
                        return 0
                y += x[i]
            y = int(y)
            if (y >= -2 ** 31) and (y <= 2 ** 31):
                return y
            else:
                return 0


        
