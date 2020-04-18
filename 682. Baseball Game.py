#https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        rounds = dict()
        points = 0
        valid_rounds = []
        for i in range(len(ops)):
            if ops[i] == '+':
                if len(valid_rounds) >= 2:
                    rounds[i] = rounds[valid_rounds[len(valid_rounds) - 1]] + rounds[valid_rounds[len(valid_rounds) - 2]]
                    valid_rounds.append(i)
                    points += rounds[i]
            elif ops[i] == 'D':
                if len(valid_rounds) >= 1:
                    rounds[i] = rounds[valid_rounds[len(valid_rounds) - 1]] * 2
                    valid_rounds.append(i)
                    points += rounds[i]
            elif ops[i] == 'C':
                if len(valid_rounds) >= 1:
                    points -= rounds[valid_rounds[len(valid_rounds) - 1]]
                    valid_rounds.pop()
            else:
                rounds[i] = int(ops[i])
                valid_rounds.append(i)
                points += int(ops[i])
        return points
                    
            
            
