#https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = []
        for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[i].append(0)
        for index in indices:
            for i in range(0, m):
                matrix[index[0]][i] += 1
            for i in range(0, n):
                matrix[i][index[1]] += 1
        
        count_cells = 0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 == 1:
                    count_cells += 1
        return count_cells
            
        
