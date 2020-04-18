#https://leetcode.com/problems/transpose-matrix/
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        m = len(A[0])
        T_A = []
        for i in range(m):
            T_A.append([])
            for j in range(n):
                T_A[i].append(0)
        for i in range(n):
            for j in range(m):
                T_A[j][i] = A[i][j]
        return T_A
        
