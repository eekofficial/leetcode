#https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        ind = self.binary_search(n)
        if ((1 + ind) * ind) / 2 == n:
            return ind
        elif ((1 + ind) * ind) / 2 > n:
            return ind - 1
        else:
            return ind + 1
        return ind
        
    def binary_search(self, n):
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            if ((1 + mid) * mid) / 2 == n:
                return mid
            elif n > ((1 + mid) * mid) / 2:
                low = mid + 1
            else:
                high = mid - 1
        return low
        
