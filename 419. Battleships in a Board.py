#https://leetcode.com/problems/battleships-in-a-board/

class Solution:
    def countBattleships(self, board) -> int:
        viewed = collections.defaultdict(dict)
        n = len(board)
        m = len(board[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X':
                    can_hor = True
                    if i - 1 >= 0:
                        if board[i - 1][j] == 'X':
                            can_hor = False
                    if i + 1 < n:
                        if board[i + 1][j] == 'X':
                            can_hor = False
                    if j - 1 >= 0:
                        if board[i][j - 1] == 'X':
                            can_hor = False
                    if can_hor:
                        count += 1
                        viewed[i][j] = True
        for j in range(m):
            for i in range(n):
                if board[i][j] == 'X' and viewed[i].get(j) == None:
                    can_ver = True
                    if j - 1 >= 0:
                        if board[i][j - 1] == 'X':
                            can_ver = False
                    if j + 1 < m:
                        if board[i][j + 1] == 'X':
                            can_ver = False
                    if i - 1 >= 0:
                        if board[i - 1][j] == 'X':
                            can_ver = False
                    if can_ver:
                        count += 1
        
        return count
