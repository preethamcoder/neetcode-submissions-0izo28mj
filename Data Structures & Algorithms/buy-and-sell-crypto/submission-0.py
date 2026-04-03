class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr_price = prices[0]
        for each in prices:
            prof = each-curr_price
            res = max(res, prof)
            if each <= curr_price:
                curr_price = each
        return res