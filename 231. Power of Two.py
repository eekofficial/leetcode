#https://leetcode.com/problems/power-of-two/

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif ((n < 1) or ((n % 2) != 0)):
            return False
        else:
            return self.isPowerOfTwo(n/2)
        
