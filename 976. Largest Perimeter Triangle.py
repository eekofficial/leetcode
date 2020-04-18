#https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, A) -> int:
        A = sorted(A, reverse=True)
        for i in range(len(A) - 2):
            if A[i + 2] < A[i] + A[i + 1] and \
                A[i] < A[i + 1] + A[i + 2] and \
                A[i + 1] < A[i] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0
