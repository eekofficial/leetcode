#https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = collections.defaultdict(str)
        t_dict = collections.defaultdict(str)
        for i in range(len(s)):
            s_dict[s[i]] += str(i)
        for i in range(len(t)):
            t_dict[t[i]] += str(i)
        values_s = list(s_dict.values())
        values_t = list(t_dict.values())
        for value_s in values_s:
            if value_s not in values_t:
                return False
            values_t.pop(values_t.index(value_s))
        return True
