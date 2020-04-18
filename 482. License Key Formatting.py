#https://leetcode.com/problems/license-key-formatting/

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = ''
        for c in S:
            if c.isalpha():
                s += c.upper()
            elif c.isdigit():
                s += c
        if len(s) == 1:
            return s
        res = []
        not_put = len(s) % K
        tmp = ''
        for i in range(not_put):
            tmp += s[i]
        if tmp != '':
            res.append(tmp)
        tmp = ''
        s = s[not_put:]
        for i in range(len(s)):
            if i % K == 0:
                if tmp != '':
                    res.append(tmp)
                tmp = ''
            tmp += s[i]
        res.append(tmp)
        return '-'.join(res)
