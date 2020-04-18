# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        pascal_triangle = []
        pascal_triangle.append([1])
        for i in range(1, numRows):
            pascal_triangle.append([])
            for j in range(i + 1):
                if j == 0:
                    pascal_triangle[i].append(1)
                elif j == i:
                    pascal_triangle[i].append(1)
                else:
                    pascal_triangle[i].append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
        return pascal_triangle
