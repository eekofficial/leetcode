#https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid) -> int:
        lower_str = 0
        i = len(grid) - 1
        count = 0
        while i >= lower_str:
            lower_col = 0
            j = len(grid[i]) - 1
            while j >= lower_col:
                if grid[i][j] >= 0:
                    lower_col = j
                else:
                    count += 1
                j -= 1
            i -= 1
        return count
            
                
