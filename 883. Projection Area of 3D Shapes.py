#https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top_projection = 0
        max_in_strings = []
        max_in_columns = []
        n = len(grid)
        for i in range(n):
            max_in_string = 0
            max_in_column = 0
            for j in range(n):
                if grid[i][j] > 0:
                    top_projection += 1
                if grid[i][j] > max_in_string:
                    max_in_string = grid[i][j]
                if grid[j][i] > max_in_column:
                    max_in_column = grid[j][i]
            max_in_strings.append(max_in_string)
            max_in_columns.append(max_in_column)
        return top_projection + sum(max_in_strings) + sum(max_in_columns)
            
                    
