#https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            mid = len(nums) // 2
            left_list = nums[:mid]
            right_list = nums[mid:]
        
            self.sortArray(left_list)
            self.sortArray(right_list)

            i = 0
            j = 0
            k = 0

            while i < len(left_list) and j < len(right_list):
                if left_list[i] < right_list[j]:
                    nums[k] = left_list[i]
                    i += 1
                else:
                    nums[k] = right_list[j]
                    j += 1
                k += 1

            while i < len(left_list):
                nums[k] = left_list[i]
                k += 1
                i += 1

            while j < len(right_list):
                nums[k] = right_list[j]
                k += 1
                j += 1
            
        return nums
