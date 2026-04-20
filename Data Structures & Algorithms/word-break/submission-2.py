class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False]*(length+1)
        dp[length] = True
        for ind in range(length-1, -1, -1):
            for word in wordDict:
                w_l = len(word)
                if ind + w_l <= length and s[ind:ind+w_l] == word:
                    dp[ind] = dp[ind+w_l]
                if dp[ind]:
                    break
        return dp[0]