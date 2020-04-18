#https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = str(num)
            sum_digits = 0
            for n in num:
                sum_digits += int(n)
            num = sum_digits
        return num
