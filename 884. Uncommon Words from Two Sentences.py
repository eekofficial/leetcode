#https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        dict_a = collections.defaultdict(int)
        dict_b = collections.defaultdict(int)
        uncommon_words = []
        for word in A.split():
            dict_a[word] += 1
        for word in B.split():
            dict_b[word] += 1
        for word, times in dict_a.items():
            if times == 1 and dict_b[word] == 0:
                uncommon_words.append(word)
        for word, times in dict_b.items():
            if times == 1 and dict_a[word] == 0:
                uncommon_words.append(word)
        return uncommon_words
        
