#https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sub_lens = [0] * len(nums)
        sub_lens[0] = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                sub_lens[i] = sub_lens[i - 1] + 1
            else:
                sub_lens[i] = 1
        return max(sub_lens)
