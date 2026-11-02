class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0:0, 1:0}

        def minCost(i):
            if i not in memo:
                memo[i] = min((minCost(i - 2) + cost[i - 2]), (minCost(i - 1) + cost[i - 1]))
            return memo[i]

        return minCost(len(cost))