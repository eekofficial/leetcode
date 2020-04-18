#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count_even = 0
        for n in nums:
            if(len(str(n))) % 2 == 0:
                count_even += 1
        return count_even
