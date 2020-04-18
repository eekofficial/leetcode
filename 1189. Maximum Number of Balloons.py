#https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_dict = collections.defaultdict(int)
        for c in text:
            text_dict[c] += 1
        return min(text_dict['o'] // 2, text_dict['l'] // 2, min([text_dict[c] for c in ('a', 'b', 'n')]))
