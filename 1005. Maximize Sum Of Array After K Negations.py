#https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        for _ in range(K):
            A[A.index(min(A))] *= -1
        return sum(A)
