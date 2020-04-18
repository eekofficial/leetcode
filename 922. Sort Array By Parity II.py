#https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1
        while left < len(A) and right > 0:
            if A[right] % 2 == 1:
                right -= 2
            else:
                if A[left] % 2 == 0:
                    left += 2
                else:
                    A[left], A[right] = A[right], A[left]
        return A
        
                
