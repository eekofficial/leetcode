# 747. Largest Number At Least Twice of Others

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        previous_max = 0
        current_max = nums[0]
        current_max_i = 0
        for i in range(len(nums)):
            if nums[i] > current_max:
                previous_max = current_max
                current_max = nums[i]
                current_max_i = i
            elif nums[i] > previous_max and nums[i] != current_max:
                previous_max = nums[i]
        if current_max / 2 >= previous_max:
            return current_max_i
        return -1
