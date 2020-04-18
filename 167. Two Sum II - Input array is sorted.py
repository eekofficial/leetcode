# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            ind = self.binary_search(numbers, target - numbers[i], i)
            if ind != -1:
                return [i + 1, ind + 1]
    
    def binary_search(self, numbers, item, i):
        low = 0
        high = len(numbers) - 1
        while low <= high:
            mid = (high + low) // 2
            if numbers[mid] == item and mid == i:
                low = mid + 1
            elif numbers[mid] == item:
                return mid
            elif item > numbers[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
