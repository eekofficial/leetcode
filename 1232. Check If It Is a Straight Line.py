#https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        first_point = coordinates[0]
        second_point = coordinates[1]
        x1, y1 = first_point[0], first_point[1]
        x2, y2 = second_point[0], second_point[1]
        if x2 - x1 == 0:
            return False
        k = (y2 - y1) / (x2 - x1)    
        c = y1 - k * x1
        straight = True
        for i in range(3, len(coordinates)):
            if coordinates[i][1] != k*coordinates[i][0] + c:
                straight = False
        return straight
