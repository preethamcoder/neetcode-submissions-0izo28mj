class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        res_len = 0
        res = ''
        for ind in range(length):
            left = ind
            right = ind
            while left >= 0 and right < length and s[left] == s[right]:
                if right - left + 1 >= res_len:
                    res_len = max(res_len, right-left+1)
                    res = s[left:right+1]
                left -= 1
                right += 1
            left = ind
            right = ind+1
            while left >= 0 and right < length and s[left] == s[right]:
                if right - left + 1 >= res_len:
                    res_len = max(res_len, right-left+1)
                    res = s[left:right+1]
                left -= 1
                right += 1
        return res