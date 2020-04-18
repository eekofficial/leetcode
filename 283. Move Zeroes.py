# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_not_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_not_zero] = nums[i]
                last_not_zero += 1
        for i in range(last_not_zero, len(nums)):
            nums[i] = 0
                
        
