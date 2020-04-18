#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[j] < nums[i]:
                        counts[i] += 1
        return counts
