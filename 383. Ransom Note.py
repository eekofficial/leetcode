# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_mag = collections.defaultdict(int)
        dict_rans = collections.defaultdict(int)
        for c in ransomNote:
            dict_rans[c] += 1
        for c in magazine:
            dict_mag[c] += 1
        for letter, times in dict_rans.items():
            if times > dict_mag[letter]:
                return False
        return True
