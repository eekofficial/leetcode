#https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points) - 1):
            current_point = points[i]
            next_point = points[i + 1]
            vertical_dist = abs(next_point[1] - current_point[1])
            horizontal_dist = abs(next_point[0] - current_point[0])
            result += max(vertical_dist, horizontal_dist)
                    
        return result
