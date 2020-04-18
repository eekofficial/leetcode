#https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels_ind = []
        vowels = []
        for i in range(len(s)):
            if s[i].lower() in ('a', 'e', 'i', 'o', 'u'):
                vowels.append(s[i])
                vowels_ind.append(i)
        if len(vowels) == 0:
            return ''.join(s)
        vowels = vowels[::-1]
        ind = 0
        for i in range(len(s)):
            if i == vowels_ind[ind]:
                s[i] = vowels[ind]
                ind += 1
            if ind >= len(vowels_ind):
                break
        return ''.join(s)
