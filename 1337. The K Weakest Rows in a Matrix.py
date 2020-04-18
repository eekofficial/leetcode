#https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = []
        for i in range(len(mat)):
            civilians = 0
            for j in range(len(mat[0]) - 1, -1, -1):
                if mat[i][j] == 1:
                    break
                else:
                    civilians += 1
            soldiers.append((i, len(mat[0]) - civilians))
        soldiers = sorted(soldiers, key=lambda x: x[1])
        return [soldiers[i][0] for i in range(k)]
                
