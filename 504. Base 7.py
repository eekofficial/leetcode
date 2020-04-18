# https://leetcode.com/problems/base-7/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        minus = False
        if -1 * num > 0:
            minus = True
            num = -1 * num
        seven_num = ''
        while num != 0:
            seven_num = str(num % 7) + seven_num
            num = num // 7
        if minus:
            seven_num = '-' + seven_num
        return seven_num
