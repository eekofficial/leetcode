#https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k % len(nums)):
            nums.insert(0, nums.pop())
        
