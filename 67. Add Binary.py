class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        else:
            b = '0' * (len(a) - len(b)) + b
        carry = 0
        res = ''
        for i in range(len(a) - 1, -1, -1):
            res = str((int(a[i]) + int(b[i]) + carry) % 2) + res
            carry = (int(a[i]) + int(b[i]) + carry) // 2
        if carry:
            res = str(carry) + res
        return res
