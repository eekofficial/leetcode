#https://leetcode.com/problems/available-captures-for-rook/

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        p_count = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_index = (i, j)
                    break
        i = rook_index[0] - 1
        j = rook_index[1]
        while i >= 0:
            if board[i][j] == 'p':
                p_count += 1
                break
            elif board[i][j] == 'B':
                break
            i -= 1
        
        i = rook_index[0] + 1
        j = rook_index[1]
        while i < 8:
            if board[i][j] == 'p':
                p_count += 1
                break
            elif board[i][j] == 'B':
                break
            i += 1    
        
        i = rook_index[0]
        j = rook_index[1] - 1
        while j >= 0:
            if board[i][j] == 'p':
                p_count += 1
                break
            elif board[i][j] == 'B':
                break
            j -= 1   
            
        i = rook_index[0]
        j = rook_index[1] + 1
        while j < 8:
            if board[i][j] == 'p':
                p_count += 1
                break
            elif board[i][j] == 'B':
                break
            j += 1   
        return p_count
