#https://leetcode.com/problems/most-common-word/

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        words_dict = collections.defaultdict(int)
        max_frequency = 0
        max_frequency_word = ''
        banned_dict = dict()
        for banned_word in banned:
            banned_dict[banned_word] = True
        word = ''
        for c in paragraph:
            if c.isalpha():
                word += c
            else:
                if word != '':
                    if banned_dict.get(word) == None:
                        words_dict[word] += 1
                        if words_dict[word] > max_frequency:
                            max_frequency = words_dict[word]
                            max_frequency_word = word
                    word = ''
        if word != '':
            if banned_dict.get(word) == None:
                words_dict[word] += 1
                if words_dict[word] > max_frequency:
                    max_frequency = words_dict[word]
                    max_frequency_word = word
        return max_frequency_word
        
        
                
                
