#https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = collections.defaultdict(int)
        for n in nums:
            nums_dict[n] += 1
        
        for num, times in nums_dict.items():
            if times > len(nums) // 2:
                return num
        
