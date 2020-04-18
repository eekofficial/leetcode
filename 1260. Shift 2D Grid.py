#https://leetcode.com/problems/shift-2d-grid/

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for i in range(k):
            last_column = [grid[k][len(grid[0]) - 1] for k in range(len(grid))]
            last_elem = last_column[len(grid) - 1]
            last_column.pop()
            new_column = [last_elem] + last_column
            for i in range(len(grid)):
                grid[i].pop()
                grid[i] = [new_column[i]] + grid[i]
        return grid
            
