#https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(len(A) - 1):
            if A[i + 1] < A[i]:
                return i
