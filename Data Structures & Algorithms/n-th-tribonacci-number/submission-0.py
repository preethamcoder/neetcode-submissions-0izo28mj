class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            first = 1
            second = 1
            third = 2
            for ind in range(3, n):
                res = first + second + third
                first = second
                second = third
                third = res
            return res