#https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_dict = collections.defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
            if nums_dict[num] == 2:
                dup = num
        for i in range(1, len(nums) + 1):
            if nums_dict[i] == 0:
                return [dup, i]
        
