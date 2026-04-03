class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        up = 2**31 - 1
        low = -1*(2**31)
        neg = False
        if x < 0:
            neg = True
            x *= -1
        while x != 0:
            dig = x % 10
            res *= 10
            res += dig
            x //= 10
        if neg:
            res *= -1
        if res < low or res > up:
            return 0
        return res