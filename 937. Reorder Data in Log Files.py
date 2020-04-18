#https://leetcode.com/problems/reorder-data-in-log-files/

from operator import itemgetter
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        first_part = []
        second_part = []
        for log in logs:
            log_2 = log.split(maxsplit=1)
            if log_2[1][0].isalpha():
                first_part.append((log_2[0], log_2[1]))
            else:
                second_part.append(log)
        first_part = sorted(first_part, key=itemgetter(1, 0))
        return [' '.join(x) for x in first_part] + second_part
                    
