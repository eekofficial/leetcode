# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        origin = [0, 0]
        for a in moves:
            if a == 'U':
                origin[1] += 1
            elif a == 'D':
                origin[1] -= 1
            elif a == 'R':
                origin[0] += 1
            elif a == 'L':
                origin[0] -= 1
        return origin == [0, 0]
