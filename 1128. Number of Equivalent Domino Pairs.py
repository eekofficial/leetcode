#https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs_dict = dict()
        count_pairs = 0
        for domino in dominoes:
            if pairs_dict.get('{}{}'.format(domino[0],domino[1])):
                pairs_dict['{}{}'.format(domino[0],domino[1])] += 1
            elif pairs_dict.get('{}{}'.format(domino[1],domino[0])):
                pairs_dict['{}{}'.format(domino[1],domino[0])] += 1
            else:
                pairs_dict['{}{}'.format(domino[0],domino[1])] = 1
        for domino, times in pairs_dict.items():
            if times > 1:
                count_pairs += (times * (times - 1)) // 2
        return count_pairs
