# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        cost.append(0)
        for i in range(2, len(cost)):
            if cost[i - 2] + cost[i] <= cost[i - 1] + cost[i]:
                cost[i] = cost[i - 2] + cost[i]
            else:
                cost[i] = cost[i - 1] + cost[i]
        return cost[len(cost) - 1]
                       
