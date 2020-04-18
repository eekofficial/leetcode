#https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = collections.defaultdict(int)
        for bill in bills:
            need_change = bill - 5
            if need_change == 0:
                change[5] += 1
            elif need_change == 5:
                if change[5] > 0:
                    change[5] -= 1
                else:
                    return False
                change[10] += 1
            elif need_change == 15:
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] > 2:
                    change[5] -= 3
                else:
                    return False
        return True
