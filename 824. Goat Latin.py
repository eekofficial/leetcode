#https://leetcode.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        goat_latin = []
        for i in range(len(words)):
            word = words[i]
            if word[0].lower() in ('a', 'e', 'i', 'o', 'u'):
                word += 'ma'
            else:
                word += word[0]
                word = word[1:]
                word += 'ma'
            word += 'a' * (i + 1)
            goat_latin.append(word)
        
        return ' '.join(goat_latin)
            
            
        
