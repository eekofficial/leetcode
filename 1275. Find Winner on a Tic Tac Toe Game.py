#https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = []
        for i in range(3):
            grid.append([])
            for j in range(3):
                grid[i].append("")
        for i in range(len(moves)):
            move = moves[i]
            if i % 2 == 0:
                grid[move[0]][move[1]] = 'X'
            else:
                grid[move[0]][move[1]] = 'O'
        if self.check_rows(grid, 'X') or self.check_columns(grid, 'X') or self.check_diagonals(grid, 'X'):
            return "A"
        elif self.check_rows(grid, 'O') or self.check_columns(grid, 'O') or self.check_diagonals(grid, 'O'):
            return "B"
        
        if self.is_empty(grid):
            return "Pending"
        else:
            return "Draw"
    
    def check_rows(self, grid, item):
        for i in range(len(grid)):
            equal_row = True
            for j in range(len(grid)):
                if grid[i][j] != item:
                    equal_row = False
            if equal_row:
                return True
        return False
    
    def check_columns(self, grid, item):
        for i in range(len(grid)):
            equal_column = True
            for j in range(len(grid)):
                if grid[j][i] != item:
                    equal_column = False
            if equal_column:
                return True
        return False
    
    def check_diagonals(self, grid, item):
        left_diag = True
        right_diag = True
        for i in range(len(grid)):
            if grid[i][i] != item:
                left_diag = False
            if grid[len(grid) - 1 - i][i] != item:
                right_diag = False
        if left_diag or right_diag:
            return True
        return False
    
    def is_empty(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == '':
                    return True
        return False
