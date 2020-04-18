#https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        not_defined = True
        increase = False
        decrease = False
        for i in range(len(A) - 1):
            if not_defined:
                if A[i] < A[i + 1]:
                    increase = True
                    not_defined = False
                elif A[i] > A[i + 1]:
                    decrease = True
                    not_defined = False
            elif increase:
                if A[i] > A[i + 1]:
                    return False
            elif decrease:
                if A[i] < A[i + 1]:
                    return False
        return True
