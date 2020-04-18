#https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0
        for num in nums:
            if num == 0:
                max_ones = max(max_ones, current_ones)
                current_ones = 0
            else:
                current_ones += 1
        max_ones = max(max_ones, current_ones)
        return max_ones
