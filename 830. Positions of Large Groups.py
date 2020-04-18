#https://leetcode.com/problems/positions-of-large-groups/

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        positions = []
        elem = S[0]
        position_first = 0
        position_last = 0
        for i in range(1, len(S)):
            if S[i] != elem:
                if i - 1 - position_first + 1 >= 3:
                    positions.append([position_first, i - 1])
                position_first = i
                elem = S[i]
        if len(S) - 1 - position_first + 1 >= 3:
            positions.append([position_first, len(S) - 1])
        return positions
