class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        first = 2
        second = 3
        for ind in range(4, n+1):
            res = first + second
            first = second
            second = res
        return res