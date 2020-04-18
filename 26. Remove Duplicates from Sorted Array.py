# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_not_duplicate = 1
        if len(nums) > 0:
            current_element = nums[0]
            for i in range(1, len(nums)):
                if nums[i] != current_element:
                    current_element = nums[i]
                    nums[last_not_duplicate] = nums[i]
                    last_not_duplicate += 1
            for i in range(last_not_duplicate, len(nums)):
                nums.pop()
            return len(nums)
        else:
            return 0
            
