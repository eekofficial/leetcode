#https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1 = '0' * (len(num2) - len(num1)) + num1
        else:
            num2 = '0' * (len(num1) - len(num2)) + num2
        carry = 0
        res = ''
        for i in range(len(num1) - 1, -1, -1):
            res = str((int(num1[i]) + int(num2[i]) + carry) % 10) + res
            carry = (int(num1[i]) + int(num2[i]) + carry) // 10
        if carry:
            res = str(carry) + res
        return res
            
