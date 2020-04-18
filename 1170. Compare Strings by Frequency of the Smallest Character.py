#https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res = [0] * len(queries)
        for i in range(len(queries)):
            count = 0
            query_f = self.min_frequency(queries[i])
            for word in words:
                if query_f < self.min_frequency(word):
                    count += 1
            res[i] = count
        return res
        
    def min_frequency(self, word):
        min_c = word[0]
        count = 1
        for i in range(1, len(word)):
            if word[i] < min_c:
                min_c = word[i]
                count = 1
            elif word[i] == min_c:
                count += 1
        return count
