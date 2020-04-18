#https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

import collections
class Solution:
    def repeatedNTimes(self, A) -> int:
        counter = collections.defaultdict(int)
        i = 0
        while True:
            counter[A[i]] += 1
            if counter[A[i]] > 1:
                break
            i += 1
        return A[i]
            
