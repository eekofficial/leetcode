#https://leetcode.com/problems/surface-area-of-3d-shapes/

class Solution:
    def surfaceArea(self, grid) -> int:
        area = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    area += 2
                    for k, l in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= k < n and 0 <= l < n:
                            over_lap = grid[k][l]
                        else:
                            over_lap = 0
                        
                        area += max(grid[i][j] - over_lap, 0)
        return area
