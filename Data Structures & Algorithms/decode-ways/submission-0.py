class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)
        zero = 0
        one = 1
        two = 0
        for ind in range(length-1, -1, -1):
            if s[ind] == '0':
                zero = 0
            else:
                zero = one
            if ind + 1 < length and (s[ind] == '1' or s[ind] == '2' and s[ind+1] in '0123456'):
                zero += two
            two = one
            one = zero
            zero = 0
        return one