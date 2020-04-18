# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int):
        pascal_triangle = [[1], [1, 1]]
        for i in range(2, rowIndex + 1):
            pascal_triangle.append([1])
            for j in range(1, i):
                pascal_triangle[i].append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
            pascal_triangle[i].append(1)
        return pascal_triangle[rowIndex]
            
        
