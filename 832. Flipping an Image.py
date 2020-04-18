#https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        odd = n % 2 == 1
        for i in range(n):
            for j in range(n // 2):
                A[i][j], A[i][n - 1 - j] = A[i][n - 1 - j], A[i][j]
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1
                if A[i][n - 1 - j] == 1:
                    A[i][n - 1 - j] = 0
                else:
                    A[i][n - 1 - j] = 1
            if odd:
                if A[i][n // 2] == 0:
                    A[i][n // 2] = 1
                else:
                    A[i][n // 2] = 0
        return A
        
