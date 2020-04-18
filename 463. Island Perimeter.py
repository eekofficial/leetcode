#https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        perimeter = 0
        values = collections.defaultdict(dict)
        for i in range(n):
            for j in range(m):
                values[i][j] = grid[i][j]
        
        for i in range(n):
            for j in range(m):
                if values[i][j] == 1:
                    square_perimeter = 4
                    if values.get(i + 1) and values.get(i + 1).get(j):
                        square_perimeter -= values[i + 1][j]
                    if values.get(i - 1) and values.get(i - 1).get(j):
                        square_perimeter -= values[i - 1][j]
                    if values.get(i) and values.get(i).get(j + 1):
                        square_perimeter -= values[i][j + 1]
                    if values.get(i) and values.get(i).get(j - 1):
                        square_perimeter -= values[i][j - 1]
                    perimeter += square_perimeter
        
        return perimeter
        
        
                
                    
                    
                    
