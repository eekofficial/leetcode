#https://leetcode.com/problems/duplicate-zeros/

class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count_zeros = 0
        elements = []
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                elements.append(arr[i + 1])
                arr[i + 1] = 0
                count_zeros += 1
                i += 2
            else:
                i += 1
        for i in range(len(arr) - 1, len(arr) - 1 - count_zeros, -1):
            arr[i] = elements.pop()
