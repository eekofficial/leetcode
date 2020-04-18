# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = collections.defaultdict(int)
        for c in s:
            s_dict[c] += 1
        for letter, times in s_dict.items():
            if times == 1:
                return s.find(letter)
        return -1
