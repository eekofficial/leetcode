#https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        one_fourth = len(arr) // 4
        num = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if arr[i] == num:
                count += 1
            else:
                num = arr[i]
                count = 1
            if count > one_fourth:
                return num
        return num
                
