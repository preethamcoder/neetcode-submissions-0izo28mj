class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        up = 2**31 - 1
        low = -1*(2**31)
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            dig = x % 10
            res *= 10
            res += dig
            x //= 10
        res *= sign
        if res < low or res > up:
            return 0
        return res