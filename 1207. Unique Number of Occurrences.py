#https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_dict = defaultdict(int)
        for n in arr:
            num_dict[n] += 1
        return len(set(num_dict.values())) == len(num_dict.values())
