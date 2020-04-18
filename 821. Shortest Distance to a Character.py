#https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        indices = []
        distance_arr = [0] * len(S)
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                indices.append(i)
        for i in range(len(distance_arr)):
            distance_arr[i] = min([abs(i - index) for index in indices])
        return distance_arr
            
                
        
