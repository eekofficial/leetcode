#https://leetcode.com/problems/smallest-range-i/

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        min_in_a = min(A)
        max_in_a = max(A)
        delta = max_in_a - min_in_a
        if K >= delta:
            return 0
        else:
            min_in_a += K
            to_subtract = max_in_a - min_in_a
            if K > to_subtract:
                return 0
            else:
                max_in_a -= K
                return max_in_a - min_in_a
            max_in_a -= delta - K
            
            
