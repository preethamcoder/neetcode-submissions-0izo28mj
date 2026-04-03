class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        first = cost[0]
        second = cost[1]
        for ind in range(2, length):
            res = cost[ind] + min(first, second)
            first = second
            second = res
        return min(first, second)