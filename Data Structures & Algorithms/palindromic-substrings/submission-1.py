class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        res = 0
        for ind in range(length):
            left = ind
            right = ind
            while left >= 0 and right < length and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            left = ind
            right = ind+1
            while left >= 0 and right < length and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res